
"""Helpers to write and query audit events."""
from __future__ import annotations

import logging
from typing import Any, Optional

from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils import timezone

from .models import AuditAction, AuditLog

logger = logging.getLogger("booking.audit")
User = get_user_model()


def _repr(obj: Any) -> str:
    try:
        return str(obj)[:255]
    except Exception:
        return type(obj).__name__


def write_audit(
    *,
    action: str,
    actor=None,
    instance=None,
    content_type: str = "",
    object_id: str = "",
    changes: Optional[dict] = None,
    metadata: Optional[dict] = None,
    request=None,
) -> AuditLog:
    if instance is not None:
        content_type = content_type or f"{instance._meta.app_label}.{instance._meta.model_name}"
        object_id = object_id or str(getattr(instance, "pk", ""))
        object_repr = _repr(instance)
    else:
        object_repr = ""

    actor_username = ""
    if actor is not None:
        actor_username = getattr(actor, "username", "") or str(actor)

    ip = ""
    ua = ""
    request_id = ""
    if request is not None:
        ip = _client_ip(request)
        ua = request.META.get("HTTP_USER_AGENT", "")[:512]
        request_id = getattr(request, "request_id", "") or request.META.get("HTTP_X_REQUEST_ID", "")

    entry = AuditLog(
        action=action,
        actor=actor if getattr(actor, "pk", None) else None,
        actor_username=actor_username,
        content_type=content_type,
        object_id=str(object_id),
        object_repr=object_repr,
        changes=changes or {},
        metadata=metadata or {},
        ip_address=ip or None,
        user_agent=ua,
        request_id=request_id,
    )
    entry.save()
    logger.info(
        "audit action=%s type=%s id=%s actor=%s",
        action,
        content_type,
        object_id,
        actor_username,
    )
    return entry


def _client_ip(request) -> str:
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR", "")


def diff_instance(old: dict, new: dict, fields: Optional[list] = None) -> dict:
    """Return {field: {"from": old, "to": new}} for changed keys."""
    keys = fields or sorted(set(old) | set(new))
    changes = {}
    for key in keys:
        ov = old.get(key)
        nv = new.get(key)
        if ov != nv:
            changes[key] = {"from": ov, "to": nv}
    return changes


@transaction.atomic
def purge_old_logs(retain_days: int = 365, batch_size: int = 1000) -> int:
    cutoff = timezone.now() - timezone.timedelta(days=retain_days)
    total = 0
    while True:
        ids = list(
            AuditLog.objects.filter(created_at__lt=cutoff)
            .order_by("created_at")
            .values_list("pk", flat=True)[:batch_size]
        )
        if not ids:
            break
        deleted, _ = AuditLog.objects.filter(pk__in=ids).delete()
        total += deleted
    return total


def recent_for_object(content_type: str, object_id: str, limit: int = 50):
    return AuditLog.objects.filter(content_type=content_type, object_id=str(object_id))[:limit]


def recent_for_user(user, limit: int = 50):
    return AuditLog.objects.filter(actor=user)[:limit]
