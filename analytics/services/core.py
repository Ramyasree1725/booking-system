"""Analytics aggregation engine for booking utilization and forecasting."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field, asdict
from datetime import date, datetime, timedelta
from decimal import Decimal
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
import statistics
import math

from django.db.models import Avg, Count, Q, Sum, F, DurationField, ExpressionWrapper
from django.db.models.functions import TruncDate, TruncHour, TruncWeek, TruncMonth
from django.utils import timezone


@dataclass
class MetricPoint:
    label: str
    value: float
    unit: str = "count"
    meta: Dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict:
        d = asdict(self)
        return d


@dataclass
class TimeSeries:
    name: str
    points: List[MetricPoint] = field(default_factory=list)

    def values(self) -> List[float]:
        return [p.value for p in self.points]

    def mean(self) -> float:
        vals = self.values()
        return statistics.mean(vals) if vals else 0.0

    def median(self) -> float:
        vals = self.values()
        return statistics.median(vals) if vals else 0.0

    def stdev(self) -> float:
        vals = self.values()
        return statistics.stdev(vals) if len(vals) > 1 else 0.0

    def moving_average(self, window: int = 7) -> List[float]:
        vals = self.values()
        if window <= 0 or not vals:
            return []
        out = []
        for i in range(len(vals)):
            start = max(0, i - window + 1)
            chunk = vals[start : i + 1]
            out.append(sum(chunk) / len(chunk))
        return out

    def as_dict(self) -> dict:
        return {"name": self.name, "points": [p.as_dict() for p in self.points]}


@dataclass
class ForecastResult:
    horizon_days: int
    predicted: List[float]
    lower: List[float]
    upper: List[float]
    method: str = "simple_trend"

    def as_dict(self) -> dict:
        return asdict(self)


class BookingAnalytics:
    """Compute booking metrics over arbitrary date ranges."""

    def __init__(self, start: Optional[datetime] = None, end: Optional[datetime] = None):
        self.end = end or timezone.now()
        self.start = start or (self.end - timedelta(days=30))

    def _base_qs(self):
        from bookings.models import Booking
        return Booking.objects.filter(
            start_datetime__gte=self.start,
            start_datetime__lt=self.end,
        )

    def count_by_status(self) -> Dict[str, int]:
        rows = self._base_qs().values("status").annotate(c=Count("id"))
        return {r["status"]: r["c"] for r in rows}

    def daily_volume(self) -> TimeSeries:
        rows = (
            self._base_qs()
            .annotate(day=TruncDate("start_datetime"))
            .values("day")
            .annotate(c=Count("id"))
            .order_by("day")
        )
        ts = TimeSeries(name="daily_volume")
        for r in rows:
            ts.points.append(MetricPoint(label=r["day"].isoformat(), value=float(r["c"])))
        return ts

    def hourly_heatmap(self) -> Dict[int, Dict[int, int]]:
        """weekday -> hour -> count"""
        grid: Dict[int, Dict[int, int]] = defaultdict(lambda: defaultdict(int))
        for dt in self._base_qs().values_list("start_datetime", flat=True):
            grid[dt.weekday()][dt.hour] += 1
        return {d: dict(h) for d, h in grid.items()}

    def resource_ranking(self, limit: int = 20) -> List[dict]:
        rows = (
            self._base_qs()
            .values("resource_id", "resource__name")
            .annotate(c=Count("id"), attendees=Sum("attendees"))
            .order_by("-c")[:limit]
        )
        return [
            {
                "resource_id": r["resource_id"],
                "name": r["resource__name"],
                "bookings": r["c"],
                "attendees": r["attendees"] or 0,
            }
            for r in rows
        ]

    def user_ranking(self, limit: int = 20) -> List[dict]:
        rows = (
            self._base_qs()
            .values("user_id", "user__username")
            .annotate(c=Count("id"))
            .order_by("-c")[:limit]
        )
        return [
            {"user_id": r["user_id"], "username": r["user__username"], "bookings": r["c"]}
            for r in rows
        ]

    def average_duration_minutes(self) -> float:
        qs = self._base_qs().annotate(
            duration=ExpressionWrapper(
                F("end_datetime") - F("start_datetime"),
                output_field=DurationField(),
            )
        )
        agg = qs.aggregate(avg=Avg("duration"))
        avg = agg["avg"]
        if avg is None:
            return 0.0
        return avg.total_seconds() / 60.0

    def cancellation_metrics(self) -> dict:
        from bookings.models import Booking
        total = self._base_qs().count()
        cancelled = self._base_qs().filter(status=Booking.Status.CANCELLED).count()
        return {
            "total": total,
            "cancelled": cancelled,
            "rate": round(cancelled / total, 4) if total else 0.0,
        }

    def lead_time_hours(self) -> dict:
        """Average hours between created_at and start_datetime."""
        deltas = []
        for created, start in self._base_qs().values_list("created_at", "start_datetime"):
            if created and start and start > created:
                deltas.append((start - created).total_seconds() / 3600.0)
        if not deltas:
            return {"mean": 0.0, "median": 0.0, "p90": 0.0}
        deltas.sort()
        p90_idx = min(len(deltas) - 1, int(len(deltas) * 0.9))
        return {
            "mean": round(statistics.mean(deltas), 2),
            "median": round(statistics.median(deltas), 2),
            "p90": round(deltas[p90_idx], 2),
        }

    def simple_trend_forecast(self, horizon_days: int = 14) -> ForecastResult:
        ts = self.daily_volume()
        vals = ts.values()
        if len(vals) < 2:
            baseline = vals[0] if vals else 0.0
            predicted = [baseline] * horizon_days
            return ForecastResult(
                horizon_days=horizon_days,
                predicted=predicted,
                lower=[max(0, p * 0.7) for p in predicted],
                upper=[p * 1.3 for p in predicted],
            )
        # linear regression y = a + b*x
        n = len(vals)
        xs = list(range(n))
        x_mean = sum(xs) / n
        y_mean = sum(vals) / n
        num = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, vals))
        den = sum((x - x_mean) ** 2 for x in xs) or 1.0
        b = num / den
        a = y_mean - b * x_mean
        predicted = []
        for i in range(horizon_days):
            y = a + b * (n + i)
            predicted.append(max(0.0, y))
        residual_std = 0.0
        if n > 2:
            residuals = [vals[i] - (a + b * i) for i in range(n)]
            residual_std = statistics.stdev(residuals)
        return ForecastResult(
            horizon_days=horizon_days,
            predicted=predicted,
            lower=[max(0.0, p - 1.28 * residual_std) for p in predicted],
            upper=[p + 1.28 * residual_std for p in predicted],
            method="linear_trend",
        )

    def full_report(self) -> dict:
        return {
            "period": {"start": self.start.isoformat(), "end": self.end.isoformat()},
            "status": self.count_by_status(),
            "daily_volume": self.daily_volume().as_dict(),
            "resource_ranking": self.resource_ranking(),
            "user_ranking": self.user_ranking(),
            "avg_duration_minutes": self.average_duration_minutes(),
            "cancellation": self.cancellation_metrics(),
            "lead_time_hours": self.lead_time_hours(),
            "forecast_14d": self.simple_trend_forecast(14).as_dict(),
            "hourly_heatmap": self.hourly_heatmap(),
        }


def compare_periods(
    current_start: datetime,
    current_end: datetime,
    previous_start: datetime,
    previous_end: datetime,
) -> dict:
    cur = BookingAnalytics(current_start, current_end)
    prev = BookingAnalytics(previous_start, previous_end)
    c_total = sum(cur.count_by_status().values())
    p_total = sum(prev.count_by_status().values())
    delta = c_total - p_total
    pct = (delta / p_total * 100.0) if p_total else 0.0
    return {
        "current_total": c_total,
        "previous_total": p_total,
        "delta": delta,
        "delta_pct": round(pct, 2),
        "current": cur.full_report(),
        "previous": prev.full_report(),
    }


def occupancy_ratio(booked_minutes: int, available_minutes: int) -> float:
    if available_minutes <= 0:
        return 0.0
    return min(1.0, booked_minutes / float(available_minutes))


def gini_coefficient(values: Sequence[float]) -> float:
    """Inequality measure for resource usage distribution."""
    vals = sorted(v for v in values if v >= 0)
    n = len(vals)
    if n == 0 or sum(vals) == 0:
        return 0.0
    cum = 0.0
    for i, v in enumerate(vals, start=1):
        cum += i * v
    return (2 * cum) / (n * sum(vals)) - (n + 1) / n
