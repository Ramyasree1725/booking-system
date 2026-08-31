
"""Notification dispatch: email templates, digests, and reminder scheduling."""
from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import timedelta
from typing import Iterable, List, Optional

from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils import timezone

logger = logging.getLogger("booking.notifications")


@dataclass
class NotificationMessage:
    subject: str
    body_text: str
    body_html: str = ""
    to: List[str] = None
    from_email: str = ""

    def __post_init__(self):
        self.to = self.to or []
        self.from_email = self.from_email or getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@localhost")


class NotificationTemplate:
    """Simple registry of notification subjects/bodies."""

    TEMPLATES = {
        "booking_created": {
            "subject": "[Booking] Created: {title}",
            "text": (
                "Your booking was created.\n\n"
                "Title: {title}\nResource: {resource}\n"
                "When: {start} – {end}\nStatus: {status}\n"
            ),
        },
        "booking_confirmed": {
            "subject": "[Booking] Confirmed: {title}",
            "text": (
                "Your booking was confirmed.\n\n"
                "Title: {title}\nResource: {resource}\n"
                "When: {start} – {end}\n"
            ),
        },
        "booking_cancelled": {
            "subject": "[Booking] Cancelled: {title}",
            "text": (
                "A booking was cancelled.\n\n"
                "Title: {title}\nResource: {resource}\n"
                "When: {start} – {end}\nReason: {reason}\n"
            ),
        },
        "booking_reminder": {
            "subject": "[Booking] Reminder: {title} starts soon",
            "text": (
                "Reminder: your booking starts in {hours} hour(s).\n\n"
                "Title: {title}\nResource: {resource}\n"
                "When: {start} – {end}\nLocation: {location}\n"
            ),
        },
        "approval_needed": {
            "subject": "[Booking] Approval needed: {title}",
            "text": (
                "A booking requires your approval.\n\n"
                "Title: {title}\nResource: {resource}\n"
                "Requester: {requester}\nWhen: {start} – {end}\n"
            ),
        },
        "booking_rejected": {
            "subject": "[Booking] Rejected: {title}",
            "text": (
                "Your booking request was rejected.\n\n"
                "Title: {title}\nResource: {resource}\n"
                "When: {start} – {end}\nReason: {reason}\n"
            ),
        },
        "daily_digest": {
            "subject": "[Booking] Daily digest for {date}",
            "text": "Daily booking digest for {date}:\n\n{body}\n",
        },
    }

    @classmethod
    def render(cls, key: str, context: dict) -> NotificationMessage:
        tpl = cls.TEMPLATES[key]
        subject = tpl["subject"].format(**context)
        body = tpl["text"].format(**context)
        return NotificationMessage(subject=subject, body_text=body, to=[])


def send_message(msg: NotificationMessage) -> bool:
    if not msg.to:
        logger.warning("notification_skipped reason=no_recipients subject=%s", msg.subject)
        return False
    try:
        if msg.body_html:
            email = EmailMultiAlternatives(msg.subject, msg.body_text, msg.from_email, msg.to)
            email.attach_alternative(msg.body_html, "text/html")
            email.send(fail_silently=False)
        else:
            send_mail(msg.subject, msg.body_text, msg.from_email, msg.to, fail_silently=False)
        logger.info("notification_sent subject=%s to=%s", msg.subject, msg.to)
        return True
    except Exception:
        logger.exception("notification_failed subject=%s to=%s", msg.subject, msg.to)
        return False


def notify_booking_event(booking, event_key: str, extra: Optional[dict] = None) -> bool:
    user = booking.user
    if not getattr(user, "notification_email", True):
        return False
    if not user.email:
        return False
    ctx = {
        "title": booking.title,
        "resource": booking.resource.name,
        "start": booking.start_datetime.strftime("%Y-%m-%d %H:%M"),
        "end": booking.end_datetime.strftime("%H:%M"),
        "status": booking.get_status_display(),
        "reason": getattr(booking, "cancellation_reason", "") or "",
        "location": booking.resource.location or "",
        "requester": user.get_full_name() or user.username,
        "hours": extra.get("hours", 1) if extra else 1,
        "date": timezone.now().date().isoformat(),
        "body": "",
    }
    if extra:
        ctx.update(extra)
    msg = NotificationTemplate.render(event_key, ctx)
    msg.to = [user.email]
    return send_message(msg)


def collect_reminders(within_hours: int = 24) -> list:
    """Return bookings that should receive a reminder soon."""
    from bookings.models import Booking

    now = timezone.now()
    window_end = now + timedelta(hours=within_hours)
    return list(
        Booking.objects.filter(
            status=Booking.Status.CONFIRMED,
            start_datetime__gt=now,
            start_datetime__lte=window_end,
        ).select_related("user", "resource")
    )


def send_reminders(within_hours: int = 24) -> int:
    sent = 0
    for booking in collect_reminders(within_hours):
        hours = max(1, int((booking.start_datetime - timezone.now()).total_seconds() // 3600))
        if notify_booking_event(booking, "booking_reminder", {"hours": hours}):
            sent += 1
    return sent


def build_daily_digest_body(bookings: Iterable) -> str:
    lines = []
    for b in bookings:
        lines.append(
            f"- {b.start_datetime:%H:%M}-{b.end_datetime:%H:%M} | {b.resource.name} | {b.title} ({b.status})"
        )
    return "\n".join(lines) if lines else "No bookings."


def send_daily_digest_for_staff(staff_users: Iterable) -> int:
    from bookings.models import Booking

    today = timezone.localdate()
    start = timezone.make_aware(datetime_combine(today))
    end = start + timedelta(days=1)
    bookings = Booking.objects.filter(
        start_datetime__gte=start,
        start_datetime__lt=end,
        status__in=[Booking.Status.CONFIRMED, Booking.Status.PENDING],
    ).select_related("resource", "user")
    body = build_daily_digest_body(bookings)
    sent = 0
    for user in staff_users:
        if not user.email:
            continue
        msg = NotificationTemplate.render(
            "daily_digest",
            {"date": today.isoformat(), "body": body, "title": "", "resource": "", "start": "", "end": "", "status": "", "reason": "", "location": "", "requester": "", "hours": 0},
        )
        msg.to = [user.email]
        if send_message(msg):
            sent += 1
    return sent


def datetime_combine(d):
    from datetime import datetime, time
    return datetime.combine(d, time.min)
