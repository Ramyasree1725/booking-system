
"""Shared validators used across the booking platform."""
from __future__ import annotations

import re
from datetime import datetime, time, timedelta
from typing import Any, Optional

from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


PHONE_RE = re.compile(r"^\+?[0-9\s\-().]{7,20}$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
HEX_COLOR_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")
RRULE_FREQ = {"DAILY", "WEEKLY", "MONTHLY", "YEARLY"}


def validate_phone(value: str) -> str:
    if not value:
        return value
    if not PHONE_RE.match(value.strip()):
        raise ValidationError(_("Enter a valid phone number."))
    return value.strip()


def validate_slug_format(value: str) -> str:
    if not SLUG_RE.match(value):
        raise ValidationError(_("Slug must be lowercase alphanumeric with hyphens."))
    return value


def validate_hex_color(value: str) -> str:
    if value and not HEX_COLOR_RE.match(value):
        raise ValidationError(_("Color must be a hex value like #3B82F6."))
    return value


def validate_future_datetime(value: datetime, grace_minutes: int = 5) -> datetime:
    if value < timezone.now() - timedelta(minutes=grace_minutes):
        raise ValidationError(_("Date/time cannot be in the past."))
    return value


def validate_time_range(start: time, end: time) -> None:
    if start >= end:
        raise ValidationError(_("Start time must be before end time."))


def validate_duration_minutes(
    duration: int,
    min_minutes: int = 15,
    max_minutes: int = 24 * 60,
) -> int:
    if duration < min_minutes:
        raise ValidationError(_("Duration is below the minimum of %(min)s minutes.") % {"min": min_minutes})
    if duration > max_minutes:
        raise ValidationError(_("Duration exceeds the maximum of %(max)s minutes.") % {"max": max_minutes})
    return duration


def validate_capacity(value: int, hard_max: int = 10000) -> int:
    if value < 1:
        raise ValidationError(_("Capacity must be at least 1."))
    if value > hard_max:
        raise ValidationError(_("Capacity exceeds system limit."))
    return value


def validate_attendee_count(attendees: int, capacity: int) -> int:
    if attendees < 1:
        raise ValidationError(_("At least one attendee is required."))
    if capacity and attendees > capacity:
        raise ValidationError(
            _("Attendees (%(a)s) exceed resource capacity (%(c)s).") % {"a": attendees, "c": capacity}
        )
    return attendees


def validate_rrule_basic(rule: str) -> str:
    if not rule:
        return rule
    upper = rule.upper()
    if "FREQ=" not in upper:
        raise ValidationError(_("RRULE must include FREQ=."))
    for freq in RRULE_FREQ:
        if f"FREQ={freq}" in upper:
            return rule
    raise ValidationError(_("Unsupported RRULE frequency."))


def validate_metadata_dict(value: Any) -> dict:
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise ValidationError(_("Metadata must be a JSON object."))
    if len(str(value)) > 50_000:
        raise ValidationError(_("Metadata payload is too large."))
    return value


def validate_amenities_list(value: Any) -> list:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValidationError(_("Amenities must be a list of strings."))
    cleaned = []
    for item in value:
        if not isinstance(item, str):
            raise ValidationError(_("Each amenity must be a string."))
        s = item.strip()
        if s:
            cleaned.append(s[:100])
    return cleaned[:50]


def validate_buffer_minutes(value: int) -> int:
    if value < 0 or value > 240:
        raise ValidationError(_("Buffer must be between 0 and 240 minutes."))
    return value


def validate_advance_days(value: int) -> int:
    if value < 1 or value > 365:
        raise ValidationError(_("Advance booking window must be 1–365 days."))
    return value


def coerce_positive_int(value: Any, default: int = 0) -> int:
    try:
        n = int(value)
        return max(0, n)
    except (TypeError, ValueError):
        return default


def safe_truncate(text: Optional[str], length: int = 200) -> str:
    if not text:
        return ""
    text = str(text).strip()
    if len(text) <= length:
        return text
    return text[: length - 1] + "…"
