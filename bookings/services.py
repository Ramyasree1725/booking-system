"""
Business logic for booking creation, conflict detection, and availability.
"""
from datetime import datetime, timedelta, time
from django.db import transaction, IntegrityError
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db.models import Q
from resources.models import Resource, AvailabilityRule, BlackoutDate
from .models import Booking


def get_buffer_delta(resource):
    minutes = resource.buffer_minutes or getattr(settings, 'BOOKING_DEFAULT_BUFFER_MINUTES', 15)
    return timedelta(minutes=minutes)


def check_blackout(resource, start, end):
    """Return True if the range overlaps any blackout."""
    blackouts = BlackoutDate.objects.filter(
        Q(resource=resource) | Q(resource__isnull=True),
        start_datetime__lt=end,
        end_datetime__gt=start,
    )
    return blackouts.exists()


def check_availability_rules(resource, start, end):
    """Verify the booking falls within defined weekly availability rules."""
    rules = list(resource.availability_rules.filter(is_active=True))
    if not rules:
        return True  # no rules = always available

    # Check each day the booking spans (usually one day)
    current = start.date()
    end_date = end.date()
    while current <= end_date:
        weekday = current.weekday()
        day_rules = [r for r in rules if r.weekday == weekday]
        if not day_rules:
            return False
        # For simplicity, require full booking window on this day to be covered
        day_start = timezone.make_aware(datetime.combine(current, time.min)) if timezone.is_naive(start) else datetime.combine(current, time.min, tzinfo=start.tzinfo)
        day_end = timezone.make_aware(datetime.combine(current, time.max)) if timezone.is_naive(end) else datetime.combine(current, time.max, tzinfo=end.tzinfo)
        segment_start = max(start, day_start)
        segment_end = min(end, day_end)
        if segment_start >= segment_end:
            current += timedelta(days=1)
            continue
        covered = False
        for rule in day_rules:
            rule_start = datetime.combine(current, rule.start_time, tzinfo=start.tzinfo)
            rule_end = datetime.combine(current, rule.end_time, tzinfo=start.tzinfo)
            if rule_start <= segment_start and rule_end >= segment_end:
                covered = True
                break
        if not covered:
            return False
        current += timedelta(days=1)
    return True


def find_conflicts(resource, start, end, exclude_booking_id=None):
    """
    Find overlapping confirmed/pending bookings, accounting for buffer time.
    """
    buffer = get_buffer_delta(resource)
    buffered_start = start - buffer
    buffered_end = end + buffer

    qs = Booking.objects.filter(
        resource=resource,
        status__in=[Booking.Status.CONFIRMED, Booking.Status.PENDING],
        start_datetime__lt=buffered_end,
        end_datetime__gt=buffered_start,
    )
    if exclude_booking_id:
        qs = qs.exclude(pk=exclude_booking_id)
    return qs


def validate_booking_slot(resource, start, end, user=None, exclude_booking_id=None):
    """Raise ValidationError if the slot is invalid."""
    if end <= start:
        raise ValidationError('End must be after start.')

    now = timezone.now()
    if start < now - timedelta(minutes=5):
        raise ValidationError('Cannot book in the past.')

    max_advance = resource.advance_booking_days or getattr(settings, 'BOOKING_MAX_ADVANCE_DAYS', 90)
    if start > now + timedelta(days=max_advance):
        raise ValidationError(f'Cannot book more than {max_advance} days in advance.')

    duration = (end - start).total_seconds() / 60
    if duration < resource.min_duration_minutes:
        raise ValidationError(f'Minimum duration is {resource.min_duration_minutes} minutes.')
    if duration > resource.max_duration_minutes:
        raise ValidationError(f'Maximum duration is {resource.max_duration_minutes} minutes.')

    if not resource.is_available:
        raise ValidationError('Resource is not available for booking.')

    if check_blackout(resource, start, end):
        raise ValidationError('This time falls within a blackout period.')

    if not check_availability_rules(resource, start, end):
        raise ValidationError('This time is outside the resource availability hours.')

    conflicts = find_conflicts(resource, start, end, exclude_booking_id)
    if conflicts.exists():
        raise ValidationError('This time slot conflicts with an existing booking (including buffer time).')


@transaction.atomic
def create_booking(*, resource, user, title, start, end, description='', attendees=1, metadata=None, force_pending=False):
    """
    Create a booking with full validation and race-condition protection.
    On PostgreSQL, an ExclusionConstraint provides the final safety net.
    """
    validate_booking_slot(resource, start, end, user)

    status = Booking.Status.PENDING if (resource.requires_approval or force_pending) else Booking.Status.CONFIRMED

    booking = Booking(
        resource=resource,
        user=user,
        title=title,
        description=description,
        start_datetime=start,
        end_datetime=end,
        status=status,
        attendees=attendees,
        metadata=metadata or {},
    )
    booking.full_clean()
    try:
        booking.save()
    except IntegrityError as e:
        # Catch exclusion constraint violation on Postgres
        raise ValidationError('Slot was just taken by another booking. Please choose another time.') from e
    return booking


def get_available_slots(resource, date, slot_minutes=30):
    """
    Return list of available (start, end) slots for a given date.
    """
    rules = resource.availability_rules.filter(is_active=True, weekday=date.weekday())
    if not rules.exists():
        return []

    slots = []
    buffer = get_buffer_delta(resource)
    day_start = timezone.make_aware(datetime.combine(date, time.min))
    day_end = timezone.make_aware(datetime.combine(date, time.max))

    # Existing bookings that day
    existing = list(Booking.objects.filter(
        resource=resource,
        status__in=[Booking.Status.CONFIRMED, Booking.Status.PENDING],
        start_datetime__date=date,
    ).order_by('start_datetime'))

    for rule in rules:
        cursor = datetime.combine(date, rule.start_time, tzinfo=day_start.tzinfo)
        rule_end = datetime.combine(date, rule.end_time, tzinfo=day_start.tzinfo)
        while cursor + timedelta(minutes=slot_minutes) <= rule_end:
            slot_end = cursor + timedelta(minutes=slot_minutes)
            # Check conflicts with buffer
            conflict = False
            for b in existing:
                if cursor < b.end_datetime + buffer and slot_end > b.start_datetime - buffer:
                    conflict = True
                    break
            if not conflict and not check_blackout(resource, cursor, slot_end):
                if cursor >= timezone.now():
                    slots.append({'start': cursor.isoformat(), 'end': slot_end.isoformat()})
            cursor += timedelta(minutes=slot_minutes)
    return slots
