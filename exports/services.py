
"""Export bookings and reports to CSV, iCal, and simple JSON dumps."""
from __future__ import annotations

import csv
import io
import json
import logging
from datetime import datetime
from typing import Iterable, List, Optional

from django.utils import timezone

logger = logging.getLogger("booking.exports")


def bookings_to_csv(bookings: Iterable) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow([
        "id", "title", "resource", "user", "start", "end", "status",
        "attendees", "created_at", "cancelled_at",
    ])
    for b in bookings:
        writer.writerow([
            str(b.pk),
            b.title,
            b.resource.name if b.resource_id else "",
            b.user.username if b.user_id else "",
            b.start_datetime.isoformat(),
            b.end_datetime.isoformat(),
            b.status,
            b.attendees,
            b.created_at.isoformat() if b.created_at else "",
            b.cancelled_at.isoformat() if b.cancelled_at else "",
        ])
    return buffer.getvalue()


def bookings_to_json(bookings: Iterable) -> str:
    payload = []
    for b in bookings:
        payload.append({
            "id": str(b.pk),
            "title": b.title,
            "resource_id": b.resource_id,
            "resource": b.resource.name if b.resource_id else None,
            "user_id": b.user_id,
            "username": b.user.username if b.user_id else None,
            "start": b.start_datetime.isoformat(),
            "end": b.end_datetime.isoformat(),
            "status": b.status,
            "attendees": b.attendees,
            "description": b.description,
        })
    return json.dumps(payload, indent=2)


def booking_to_ical_event(booking) -> str:
    """Return a single VEVENT block (no calendar wrapper)."""
    uid = f"{booking.pk}@bookingsystem.local"
    dtstamp = timezone.now().strftime("%Y%m%dT%H%M%SZ")
    dtstart = booking.start_datetime.strftime("%Y%m%dT%H%M%SZ")
    dtend = booking.end_datetime.strftime("%Y%m%dT%H%M%SZ")
    summary = _ical_escape(booking.title)
    description = _ical_escape(booking.description or "")
    location = _ical_escape(booking.resource.location if booking.resource_id else "")
    lines = [
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"DTSTAMP:{dtstamp}",
        f"DTSTART:{dtstart}",
        f"DTEND:{dtend}",
        f"SUMMARY:{summary}",
        f"DESCRIPTION:{description}",
        f"LOCATION:{location}",
        f"STATUS:{_ical_status(booking.status)}",
        "END:VEVENT",
    ]
    return "\r\n".join(lines)


def bookings_to_ical(bookings: Iterable, cal_name: str = "Booking System") -> str:
    header = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Booking System//EN",
        f"X-WR-CALNAME:{_ical_escape(cal_name)}",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
    ]
    events = [booking_to_ical_event(b) for b in bookings]
    footer = ["END:VCALENDAR"]
    return "\r\n".join(header + events + footer) + "\r\n"


def _ical_escape(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace(";", "\\;")
        .replace(",", "\\,")
        .replace("\n", "\\n")
    )


def _ical_status(status: str) -> str:
    mapping = {
        "confirmed": "CONFIRMED",
        "cancelled": "CANCELLED",
        "pending": "TENTATIVE",
        "rejected": "CANCELLED",
        "completed": "CONFIRMED",
        "no_show": "CONFIRMED",
    }
    return mapping.get(status, "CONFIRMED")


def utilization_rows_to_csv(rows: List[list]) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    for row in rows:
        writer.writerow(row)
    return buffer.getvalue()


def resources_to_csv(resources: Iterable) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow([
        "id", "name", "slug", "location", "capacity", "status",
        "buffer_minutes", "min_duration", "max_duration", "is_public",
    ])
    for r in resources:
        writer.writerow([
            r.pk, r.name, r.slug, r.location, r.capacity, r.status,
            r.buffer_minutes, r.min_duration_minutes, r.max_duration_minutes, r.is_public,
        ])
    return buffer.getvalue()
