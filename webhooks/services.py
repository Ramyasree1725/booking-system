
"""Outbound webhooks for booking lifecycle events."""
from __future__ import annotations

import hashlib
import hmac
import json
import logging
from typing import Any, Dict, Optional

from django.conf import settings
from django.utils import timezone

logger = logging.getLogger("booking.webhooks")


class WebhookEvent:
    BOOKING_CREATED = "booking.created"
    BOOKING_UPDATED = "booking.updated"
    BOOKING_CANCELLED = "booking.cancelled"
    BOOKING_APPROVED = "booking.approved"
    BOOKING_REJECTED = "booking.rejected"
    RESOURCE_CREATED = "resource.created"
    RESOURCE_UPDATED = "resource.updated"


def sign_payload(secret: str, body: bytes) -> str:
    return hmac.new(secret.encode("utf-8"), body, hashlib.sha256).hexdigest()


def build_payload(event: str, data: dict, delivery_id: str = "") -> dict:
    return {
        "id": delivery_id or f"evt_{timezone.now().strftime('%Y%m%d%H%M%S%f')}",
        "event": event,
        "created_at": timezone.now().isoformat(),
        "data": data,
    }


def booking_payload(booking) -> dict:
    return {
        "id": str(booking.pk),
        "title": booking.title,
        "status": booking.status,
        "resource_id": booking.resource_id,
        "resource_name": booking.resource.name if booking.resource_id else None,
        "user_id": booking.user_id,
        "start": booking.start_datetime.isoformat(),
        "end": booking.end_datetime.isoformat(),
        "attendees": booking.attendees,
    }


def deliver_webhook(
    url: str,
    event: str,
    data: dict,
    secret: str = "",
    timeout: float = 5.0,
) -> bool:
    """Best-effort HTTP POST. Uses urllib to avoid hard dependency on requests at import."""
    import urllib.error
    import urllib.request

    payload = build_payload(event, data)
    body = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "BookingSystem-Webhook/1.0",
        "X-Webhook-Event": event,
    }
    if secret:
        headers["X-Webhook-Signature"] = sign_payload(secret, body)
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            ok = 200 <= resp.status < 300
            logger.info("webhook_delivered event=%s url=%s status=%s", event, url, resp.status)
            return ok
    except urllib.error.URLError as exc:
        logger.warning("webhook_failed event=%s url=%s error=%s", event, url, exc)
        return False


def dispatch_booking_event(event: str, booking, endpoints: Optional[list] = None) -> int:
    """
    endpoints: list of dicts {url, secret, events?}
    If None, reads from settings.BOOKING_WEBHOOKS.
    """
    endpoints = endpoints if endpoints is not None else getattr(settings, "BOOKING_WEBHOOKS", [])
    data = booking_payload(booking)
    delivered = 0
    for ep in endpoints:
        url = ep.get("url")
        if not url:
            continue
        allowed = ep.get("events")
        if allowed and event not in allowed:
            continue
        secret = ep.get("secret", "")
        if deliver_webhook(url, event, data, secret=secret):
            delivered += 1
    return delivered
