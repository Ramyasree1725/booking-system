
"""Reporting services: utilization, occupancy, and booking summaries."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, asdict
from datetime import date, datetime, timedelta
from typing import Any, Dict, Iterable, List, Optional, Tuple

from django.db.models import Avg, Count, DurationField, ExpressionWrapper, F, Q, Sum
from django.db.models.functions import TruncDate, TruncMonth, TruncWeek
from django.utils import timezone

from bookings.models import Booking
from resources.models import Resource


@dataclass
class UtilizationRow:
    resource_id: int
    resource_name: str
    date: str
    booked_minutes: int
    available_minutes: int
    utilization: float
    booking_count: int

    def as_dict(self) -> dict:
        return asdict(self)


@dataclass
class OccupancySnapshot:
    resource_id: int
    resource_name: str
    capacity: int
    current_attendees: int
    occupancy_pct: float
    status: str


def _default_range(days: int = 30) -> Tuple[datetime, datetime]:
    end = timezone.now()
    start = end - timedelta(days=days)
    return start, end


def booking_status_breakdown(
    start: Optional[datetime] = None,
    end: Optional[datetime] = None,
    resource_id: Optional[int] = None,
) -> Dict[str, int]:
    start, end = start or _default_range()[0], end or _default_range()[1]
    qs = Booking.objects.filter(start_datetime__gte=start, start_datetime__lt=end)
    if resource_id:
        qs = qs.filter(resource_id=resource_id)
    rows = qs.values("status").annotate(c=Count("id"))
    return {r["status"]: r["c"] for r in rows}


def bookings_per_day(
    start: Optional[datetime] = None,
    end: Optional[datetime] = None,
    resource_id: Optional[int] = None,
) -> List[dict]:
    start, end = start or _default_range()[0], end or _default_range()[1]
    qs = Booking.objects.filter(
        start_datetime__gte=start,
        start_datetime__lt=end,
        status__in=[Booking.Status.CONFIRMED, Booking.Status.COMPLETED],
    )
    if resource_id:
        qs = qs.filter(resource_id=resource_id)
    rows = (
        qs.annotate(day=TruncDate("start_datetime"))
        .values("day")
        .annotate(count=Count("id"))
        .order_by("day")
    )
    return [{"date": r["day"].isoformat(), "count": r["count"]} for r in rows]


def bookings_per_week(
    start: Optional[datetime] = None,
    end: Optional[datetime] = None,
) -> List[dict]:
    start, end = start or _default_range(90)[0], end or _default_range(90)[1]
    rows = (
        Booking.objects.filter(
            start_datetime__gte=start,
            start_datetime__lt=end,
            status__in=[Booking.Status.CONFIRMED, Booking.Status.COMPLETED],
        )
        .annotate(week=TruncWeek("start_datetime"))
        .values("week")
        .annotate(count=Count("id"))
        .order_by("week")
    )
    return [{"week": r["week"].isoformat(), "count": r["count"]} for r in rows]


def top_resources_by_bookings(
    start: Optional[datetime] = None,
    end: Optional[datetime] = None,
    limit: int = 10,
) -> List[dict]:
    start, end = start or _default_range()[0], end or _default_range()[1]
    rows = (
        Booking.objects.filter(
            start_datetime__gte=start,
            start_datetime__lt=end,
            status__in=[Booking.Status.CONFIRMED, Booking.Status.COMPLETED, Booking.Status.PENDING],
        )
        .values("resource_id", "resource__name")
        .annotate(count=Count("id"))
        .order_by("-count")[:limit]
    )
    return [
        {"resource_id": r["resource_id"], "name": r["resource__name"], "count": r["count"]}
        for r in rows
    ]


def top_users_by_bookings(
    start: Optional[datetime] = None,
    end: Optional[datetime] = None,
    limit: int = 10,
) -> List[dict]:
    start, end = start or _default_range()[0], end or _default_range()[1]
    rows = (
        Booking.objects.filter(
            start_datetime__gte=start,
            start_datetime__lt=end,
        )
        .values("user_id", "user__username", "user__email")
        .annotate(count=Count("id"))
        .order_by("-count")[:limit]
    )
    return [
        {
            "user_id": r["user_id"],
            "username": r["user__username"],
            "email": r["user__email"],
            "count": r["count"],
        }
        for r in rows
    ]


def average_booking_duration(
    start: Optional[datetime] = None,
    end: Optional[datetime] = None,
    resource_id: Optional[int] = None,
) -> Optional[float]:
    start, end = start or _default_range()[0], end or _default_range()[1]
    qs = Booking.objects.filter(
        start_datetime__gte=start,
        start_datetime__lt=end,
        status__in=[Booking.Status.CONFIRMED, Booking.Status.COMPLETED],
    )
    if resource_id:
        qs = qs.filter(resource_id=resource_id)
    qs = qs.annotate(
        duration=ExpressionWrapper(F("end_datetime") - F("start_datetime"), output_field=DurationField())
    )
    agg = qs.aggregate(avg=Avg("duration"))
    avg = agg["avg"]
    if avg is None:
        return None
    return avg.total_seconds() / 60.0


def cancellation_rate(
    start: Optional[datetime] = None,
    end: Optional[datetime] = None,
) -> dict:
    start, end = start or _default_range()[0], end or _default_range()[1]
    qs = Booking.objects.filter(created_at__gte=start, created_at__lt=end)
    total = qs.count()
    cancelled = qs.filter(status=Booking.Status.CANCELLED).count()
    rate = (cancelled / total) if total else 0.0
    return {"total": total, "cancelled": cancelled, "rate": round(rate, 4)}


def no_show_rate(
    start: Optional[datetime] = None,
    end: Optional[datetime] = None,
) -> dict:
    start, end = start or _default_range()[0], end or _default_range()[1]
    qs = Booking.objects.filter(
        start_datetime__gte=start,
        start_datetime__lt=end,
        status__in=[Booking.Status.COMPLETED, Booking.Status.NO_SHOW, Booking.Status.CONFIRMED],
    )
    total = qs.count()
    no_shows = qs.filter(status=Booking.Status.NO_SHOW).count()
    rate = (no_shows / total) if total else 0.0
    return {"total": total, "no_shows": no_shows, "rate": round(rate, 4)}


def utilization_for_resource(
    resource: Resource,
    day: date,
    open_minutes: int = 9 * 60,
) -> UtilizationRow:
    start = timezone.make_aware(datetime.combine(day, datetime.min.time()))
    end = start + timedelta(days=1)
    bookings = Booking.objects.filter(
        resource=resource,
        status__in=[Booking.Status.CONFIRMED, Booking.Status.COMPLETED],
        start_datetime__lt=end,
        end_datetime__gt=start,
    )
    booked = 0
    for b in bookings:
        s = max(b.start_datetime, start)
        e = min(b.end_datetime, end)
        booked += max(0, int((e - s).total_seconds() // 60))
    util = min(1.0, booked / open_minutes) if open_minutes else 0.0
    return UtilizationRow(
        resource_id=resource.pk,
        resource_name=resource.name,
        date=day.isoformat(),
        booked_minutes=booked,
        available_minutes=open_minutes,
        utilization=round(util, 4),
        booking_count=bookings.count(),
    )


def utilization_matrix(
    resources: Iterable[Resource],
    start_day: date,
    end_day: date,
    open_minutes: int = 9 * 60,
) -> List[UtilizationRow]:
    rows: List[UtilizationRow] = []
    day = start_day
    resource_list = list(resources)
    while day <= end_day:
        for resource in resource_list:
            rows.append(utilization_for_resource(resource, day, open_minutes))
        day += timedelta(days=1)
    return rows


def peak_hours_histogram(
    start: Optional[datetime] = None,
    end: Optional[datetime] = None,
    resource_id: Optional[int] = None,
) -> Dict[int, int]:
    """Return mapping hour -> booking starts count."""
    start, end = start or _default_range()[0], end or _default_range()[1]
    qs = Booking.objects.filter(
        start_datetime__gte=start,
        start_datetime__lt=end,
        status__in=[Booking.Status.CONFIRMED, Booking.Status.COMPLETED],
    )
    if resource_id:
        qs = qs.filter(resource_id=resource_id)
    hist: Dict[int, int] = defaultdict(int)
    for dt in qs.values_list("start_datetime", flat=True):
        hist[dt.hour] += 1
    return dict(sorted(hist.items()))


def dashboard_summary(days: int = 30) -> dict:
    start, end = _default_range(days)
    return {
        "period": {"start": start.isoformat(), "end": end.isoformat(), "days": days},
        "status_breakdown": booking_status_breakdown(start, end),
        "bookings_per_day": bookings_per_day(start, end),
        "top_resources": top_resources_by_bookings(start, end),
        "top_users": top_users_by_bookings(start, end),
        "avg_duration_minutes": average_booking_duration(start, end),
        "cancellation": cancellation_rate(start, end),
        "no_show": no_show_rate(start, end),
        "peak_hours": peak_hours_histogram(start, end),
        "active_resources": Resource.objects.filter(status=Resource.Status.ACTIVE).count(),
        "total_bookings": Booking.objects.filter(start_datetime__gte=start, start_datetime__lt=end).count(),
    }


def export_utilization_csv_rows(rows: List[UtilizationRow]) -> List[List[Any]]:
    header = [
        "resource_id",
        "resource_name",
        "date",
        "booked_minutes",
        "available_minutes",
        "utilization",
        "booking_count",
    ]
    data = [header]
    for r in rows:
        data.append([
            r.resource_id,
            r.resource_name,
            r.date,
            r.booked_minutes,
            r.available_minutes,
            r.utilization,
            r.booking_count,
        ])
    return data
