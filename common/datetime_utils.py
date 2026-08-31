
"""Date, time, and availability calculation helpers for the booking platform."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta
from typing import Iterable, Iterator, List, Optional, Sequence, Tuple
from zoneinfo import ZoneInfo

from django.utils import timezone


UTC = ZoneInfo("UTC")


@dataclass(frozen=True, order=True)
class TimeWindow:
    """Immutable half-open interval [start, end)."""

    start: datetime
    end: datetime

    def __post_init__(self) -> None:
        if self.end <= self.start:
            raise ValueError("TimeWindow end must be after start")

    @property
    def duration(self) -> timedelta:
        return self.end - self.start

    @property
    def duration_minutes(self) -> int:
        return int(self.duration.total_seconds() // 60)

    def overlaps(self, other: "TimeWindow") -> bool:
        return self.start < other.end and other.start < self.end

    def contains(self, instant: datetime) -> bool:
        return self.start <= instant < self.end

    def intersection(self, other: "TimeWindow") -> Optional["TimeWindow"]:
        s = max(self.start, other.start)
        e = min(self.end, other.end)
        if s < e:
            return TimeWindow(s, e)
        return None

    def expand(self, before: timedelta = timedelta(), after: timedelta = timedelta()) -> "TimeWindow":
        return TimeWindow(self.start - before, self.end + after)

    def shift(self, delta: timedelta) -> "TimeWindow":
        return TimeWindow(self.start + delta, self.end + delta)

    def to_tuple(self) -> Tuple[datetime, datetime]:
        return self.start, self.end

    def isoformat(self) -> dict:
        return {"start": self.start.isoformat(), "end": self.end.isoformat()}


@dataclass
class DaySchedule:
    """Availability windows for a single calendar day."""

    day: date
    windows: List[TimeWindow] = field(default_factory=list)

    def add(self, start: time, end: time, tz: ZoneInfo = UTC) -> None:
        s = datetime.combine(self.day, start, tzinfo=tz)
        e = datetime.combine(self.day, end, tzinfo=tz)
        if e > s:
            self.windows.append(TimeWindow(s, e))

    def merge_overlapping(self) -> None:
        if not self.windows:
            return
        ordered = sorted(self.windows, key=lambda w: w.start)
        merged: List[TimeWindow] = [ordered[0]]
        for w in ordered[1:]:
            last = merged[-1]
            if w.start <= last.end:
                merged[-1] = TimeWindow(last.start, max(last.end, w.end))
            else:
                merged.append(w)
        self.windows = merged

    def subtract(self, blocked: TimeWindow) -> None:
        result: List[TimeWindow] = []
        for w in self.windows:
            inter = w.intersection(blocked)
            if inter is None:
                result.append(w)
                continue
            if w.start < inter.start:
                result.append(TimeWindow(w.start, inter.start))
            if inter.end < w.end:
                result.append(TimeWindow(inter.end, w.end))
        self.windows = result

    def free_slots(self, slot_minutes: int, buffer: timedelta = timedelta()) -> List[TimeWindow]:
        slots: List[TimeWindow] = []
        step = timedelta(minutes=slot_minutes)
        for w in self.windows:
            cursor = w.start
            while cursor + step <= w.end:
                candidate = TimeWindow(cursor, cursor + step)
                expanded = candidate.expand(before=buffer, after=buffer)
                # still within day window after buffer is caller's responsibility
                slots.append(candidate)
                cursor += step
        return slots


def ensure_aware(dt: datetime, default_tz: ZoneInfo = UTC) -> datetime:
    if timezone.is_naive(dt):
        return timezone.make_aware(dt, default_tz)
    return dt


def floor_to_minutes(dt: datetime, minutes: int = 15) -> datetime:
    discard = timedelta(
        minutes=dt.minute % minutes,
        seconds=dt.second,
        microseconds=dt.microsecond,
    )
    return dt - discard


def ceil_to_minutes(dt: datetime, minutes: int = 15) -> datetime:
    floored = floor_to_minutes(dt, minutes)
    if floored == dt:
        return dt
    return floored + timedelta(minutes=minutes)


def iter_dates(start: date, end: date) -> Iterator[date]:
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)


def business_days_between(start: date, end: date) -> int:
    count = 0
    for d in iter_dates(start, end):
        if d.weekday() < 5:
            count += 1
    return count


def next_business_day(d: date) -> date:
    nxt = d + timedelta(days=1)
    while nxt.weekday() >= 5:
        nxt += timedelta(days=1)
    return nxt


def previous_business_day(d: date) -> date:
    prev = d - timedelta(days=1)
    while prev.weekday() >= 5:
        prev -= timedelta(days=1)
    return prev


def combine_date_time(d: date, t: time, tz: ZoneInfo = UTC) -> datetime:
    return datetime.combine(d, t, tzinfo=tz)


def split_by_day(window: TimeWindow) -> List[TimeWindow]:
    """Split a multi-day window into per-day segments."""
    parts: List[TimeWindow] = []
    current = window.start
    while current.date() < window.end.date():
        day_end = datetime.combine(current.date(), time.max, tzinfo=current.tzinfo)
        # use next midnight instead
        next_midnight = datetime.combine(current.date() + timedelta(days=1), time.min, tzinfo=current.tzinfo)
        parts.append(TimeWindow(current, min(next_midnight, window.end)))
        current = next_midnight
    if current < window.end:
        parts.append(TimeWindow(current, window.end))
    return parts


def compress_windows(windows: Sequence[TimeWindow]) -> List[TimeWindow]:
    if not windows:
        return []
    ordered = sorted(windows, key=lambda w: w.start)
    out: List[TimeWindow] = [ordered[0]]
    for w in ordered[1:]:
        last = out[-1]
        if w.start <= last.end:
            out[-1] = TimeWindow(last.start, max(last.end, w.end))
        else:
            out.append(w)
    return out


def subtract_all(available: Sequence[TimeWindow], blocked: Sequence[TimeWindow]) -> List[TimeWindow]:
    result = list(available)
    for b in blocked:
        next_result: List[TimeWindow] = []
        for a in result:
            inter = a.intersection(b)
            if inter is None:
                next_result.append(a)
            else:
                if a.start < inter.start:
                    next_result.append(TimeWindow(a.start, inter.start))
                if inter.end < a.end:
                    next_result.append(TimeWindow(inter.end, a.end))
        result = next_result
    return result


def find_first_slot(
    available: Sequence[TimeWindow],
    duration: timedelta,
    after: Optional[datetime] = None,
) -> Optional[TimeWindow]:
    after = after or timezone.now()
    for w in available:
        start = max(w.start, after)
        if start + duration <= w.end:
            return TimeWindow(start, start + duration)
    return None


def humanize_duration(minutes: int) -> str:
    if minutes < 60:
        return f"{minutes} min"
    hours, mins = divmod(minutes, 60)
    if mins == 0:
        return f"{hours}h"
    return f"{hours}h {mins}m"


def humanize_window(window: TimeWindow, fmt: str = "%Y-%m-%d %H:%M") -> str:
    return f"{window.start.strftime(fmt)} – {window.end.strftime('%H:%M')}"


def is_same_day(a: datetime, b: datetime) -> bool:
    return a.date() == b.date()


def week_start(d: date, week_starts_on: int = 0) -> date:
    """week_starts_on: 0=Monday … 6=Sunday"""
    return d - timedelta(days=(d.weekday() - week_starts_on) % 7)


def week_end(d: date, week_starts_on: int = 0) -> date:
    return week_start(d, week_starts_on) + timedelta(days=6)


def month_bounds(d: date) -> Tuple[date, date]:
    start = d.replace(day=1)
    if d.month == 12:
        end = date(d.year + 1, 1, 1) - timedelta(days=1)
    else:
        end = date(d.year, d.month + 1, 1) - timedelta(days=1)
    return start, end


def parse_iso_datetime(value: str) -> datetime:
    """Parse ISO-8601 datetime, ensuring timezone awareness."""
    raw = value.strip()
    if raw.endswith("Z"):
        raw = raw[:-1] + "+00:00"
    dt = datetime.fromisoformat(raw)
    return ensure_aware(dt)


def clamp_to_range(value: datetime, low: datetime, high: datetime) -> datetime:
    return max(low, min(high, value))


def overlapping_pairs(windows: Sequence[TimeWindow]) -> List[Tuple[TimeWindow, TimeWindow]]:
    pairs: List[Tuple[TimeWindow, TimeWindow]] = []
    ordered = sorted(windows, key=lambda w: w.start)
    for i, a in enumerate(ordered):
        for b in ordered[i + 1 :]:
            if b.start >= a.end:
                break
            if a.overlaps(b):
                pairs.append((a, b))
    return pairs


def total_minutes(windows: Iterable[TimeWindow]) -> int:
    return sum(w.duration_minutes for w in windows)


def density_score(booked: Sequence[TimeWindow], available: Sequence[TimeWindow]) -> float:
    avail = total_minutes(available)
    if avail <= 0:
        return 0.0
    used = total_minutes(booked)
    return min(1.0, used / avail)
