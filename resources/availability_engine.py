
"""High-level availability engine combining rules, blackouts, buffers, and bookings."""
from __future__ import annotations

from datetime import date, datetime, time, timedelta
from typing import List, Optional, Sequence

from django.db.models import Q
from django.utils import timezone

from common.datetime_utils import (
    DaySchedule,
    TimeWindow,
    compress_windows,
    ensure_aware,
    subtract_all,
)
from resources.models import AvailabilityRule, BlackoutDate, Resource
from bookings.models import Booking


class AvailabilityEngine:
    def __init__(self, resource: Resource):
        self.resource = resource
        self.buffer = timedelta(minutes=resource.buffer_minutes or 0)

    def rules_for_day(self, day: date) -> List[AvailabilityRule]:
        return list(
            self.resource.availability_rules.filter(is_active=True, weekday=day.weekday())
        )

    def blackouts_overlapping(self, start: datetime, end: datetime) -> List[BlackoutDate]:
        return list(
            BlackoutDate.objects.filter(
                Q(resource=self.resource) | Q(resource__isnull=True),
                start_datetime__lt=end,
                end_datetime__gt=start,
            )
        )

    def bookings_overlapping(self, start: datetime, end: datetime, exclude_id=None) -> List[Booking]:
        qs = Booking.objects.filter(
            resource=self.resource,
            status__in=[Booking.Status.CONFIRMED, Booking.Status.PENDING],
            start_datetime__lt=end,
            end_datetime__gt=start,
        )
        if exclude_id:
            qs = qs.exclude(pk=exclude_id)
        return list(qs)

    def open_windows_for_day(self, day: date) -> List[TimeWindow]:
        schedule = DaySchedule(day=day)
        tz = timezone.get_current_timezone()
        for rule in self.rules_for_day(day):
            schedule.add(rule.start_time, rule.end_time, tz=tz)
        schedule.merge_overlapping()
        return schedule.windows

    def blocked_windows(self, start: datetime, end: datetime, exclude_id=None) -> List[TimeWindow]:
        blocked: List[TimeWindow] = []
        for b in self.blackouts_overlapping(start, end):
            blocked.append(TimeWindow(ensure_aware(b.start_datetime), ensure_aware(b.end_datetime)))
        for booking in self.bookings_overlapping(start, end, exclude_id=exclude_id):
            w = TimeWindow(ensure_aware(booking.start_datetime), ensure_aware(booking.end_datetime))
            blocked.append(w.expand(before=self.buffer, after=self.buffer))
        return compress_windows(blocked)

    def free_windows_for_day(self, day: date, exclude_id=None) -> List[TimeWindow]:
        open_w = self.open_windows_for_day(day)
        if not open_w:
            return []
        day_start = open_w[0].start.replace(hour=0, minute=0, second=0, microsecond=0)
        day_end = day_start + timedelta(days=1)
        blocked = self.blocked_windows(day_start, day_end, exclude_id=exclude_id)
        return subtract_all(open_w, blocked)

    def slots_for_day(
        self,
        day: date,
        slot_minutes: Optional[int] = None,
        exclude_id=None,
    ) -> List[dict]:
        slot_minutes = slot_minutes or self.resource.min_duration_minutes or 30
        free = self.free_windows_for_day(day, exclude_id=exclude_id)
        step = timedelta(minutes=slot_minutes)
        now = timezone.now()
        result = []
        for window in free:
            cursor = window.start
            while cursor + step <= window.end:
                if cursor >= now:
                    result.append({
                        "start": cursor.isoformat(),
                        "end": (cursor + step).isoformat(),
                    })
                cursor += step
        return result

    def is_slot_free(self, start: datetime, end: datetime, exclude_id=None) -> bool:
        start, end = ensure_aware(start), ensure_aware(end)
        if end <= start:
            return False
        # Must be inside open windows for each day spanned
        day = start.date()
        end_day = end.date()
        while day <= end_day:
            free = self.free_windows_for_day(day, exclude_id=exclude_id)
            day_start = max(start, datetime.combine(day, time.min, tzinfo=start.tzinfo))
            day_end = min(end, datetime.combine(day + timedelta(days=1), time.min, tzinfo=start.tzinfo))
            if day_start >= day_end:
                day += timedelta(days=1)
                continue
            covered = False
            for w in free:
                if w.start <= day_start and w.end >= day_end:
                    covered = True
                    break
            if not covered:
                return False
            day += timedelta(days=1)
        return True

    def next_available(
        self,
        after: Optional[datetime] = None,
        duration_minutes: Optional[int] = None,
        search_days: int = 14,
    ) -> Optional[dict]:
        after = ensure_aware(after or timezone.now())
        duration_minutes = duration_minutes or self.resource.min_duration_minutes or 30
        duration = timedelta(minutes=duration_minutes)
        for offset in range(search_days):
            day = (after + timedelta(days=offset)).date()
            for window in self.free_windows_for_day(day):
                start = max(window.start, after)
                if start + duration <= window.end:
                    return {"start": start.isoformat(), "end": (start + duration).isoformat()}
        return None

# availability engine refinements
