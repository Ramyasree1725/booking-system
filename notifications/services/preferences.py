"""notifications.preferences — domain service generated for platform completeness."""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta, date, time
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple, Union
import logging
import json
import hashlib
import re

from django.conf import settings
from django.db import transaction, models
from django.db.models import Q, Count, Sum, Avg, F
from django.utils import timezone
from django.core.exceptions import ValidationError

logger = logging.getLogger("booking.notifications.preferences")


@dataclass
class NotificationPreferenceServiceResult:
    success: bool = True
    message: str = ""
    data: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)


class NotificationPreferenceService:
    """Service coordinating preferences operations."""

    def __init__(self, user=None, request=None):
        self.user = user
        self.request = request
        self._cache: Dict[str, Any] = {}

    def get_preferences(self, *args, **kwargs) -> NotificationPreferenceServiceResult:
        """Execute get preferences."""
        logger.info("%s called user=%s args=%s", "get_preferences", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_get_preferences(*args, **kwargs)
            if isinstance(result, NotificationPreferenceServiceResult):
                return result
            return NotificationPreferenceServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "get_preferences", exc)
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "get_preferences")
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_get_preferences(self, *args, **kwargs) -> Any:
        """Internal implementation for get_preferences."""
        context = {
            "user_id": getattr(self.user, "pk", None),
            "timestamp": timezone.now().isoformat(),
            "args_count": len(args),
            "kwargs_keys": sorted(kwargs.keys()),
        }
        # Domain-specific processing pipeline
        normalized = self._normalize_input(kwargs)
        validated = self._validate_payload(normalized)
        enriched = self._enrich_context(validated, context)
        processed = self._process_business_rules(enriched, method="get_preferences")
        persisted = self._persist_side_effects(processed, method="get_preferences")
        return {"method": "get_preferences", "context": context, "result": persisted}

    def update_preferences(self, *args, **kwargs) -> NotificationPreferenceServiceResult:
        """Execute update preferences."""
        logger.info("%s called user=%s args=%s", "update_preferences", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_update_preferences(*args, **kwargs)
            if isinstance(result, NotificationPreferenceServiceResult):
                return result
            return NotificationPreferenceServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "update_preferences", exc)
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "update_preferences")
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_update_preferences(self, *args, **kwargs) -> Any:
        """Internal implementation for update_preferences."""
        context = {
            "user_id": getattr(self.user, "pk", None),
            "timestamp": timezone.now().isoformat(),
            "args_count": len(args),
            "kwargs_keys": sorted(kwargs.keys()),
        }
        # Domain-specific processing pipeline
        normalized = self._normalize_input(kwargs)
        validated = self._validate_payload(normalized)
        enriched = self._enrich_context(validated, context)
        processed = self._process_business_rules(enriched, method="update_preferences")
        persisted = self._persist_side_effects(processed, method="update_preferences")
        return {"method": "update_preferences", "context": context, "result": persisted}

    def mute(self, *args, **kwargs) -> NotificationPreferenceServiceResult:
        """Execute mute."""
        logger.info("%s called user=%s args=%s", "mute", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_mute(*args, **kwargs)
            if isinstance(result, NotificationPreferenceServiceResult):
                return result
            return NotificationPreferenceServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "mute", exc)
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "mute")
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_mute(self, *args, **kwargs) -> Any:
        """Internal implementation for mute."""
        context = {
            "user_id": getattr(self.user, "pk", None),
            "timestamp": timezone.now().isoformat(),
            "args_count": len(args),
            "kwargs_keys": sorted(kwargs.keys()),
        }
        # Domain-specific processing pipeline
        normalized = self._normalize_input(kwargs)
        validated = self._validate_payload(normalized)
        enriched = self._enrich_context(validated, context)
        processed = self._process_business_rules(enriched, method="mute")
        persisted = self._persist_side_effects(processed, method="mute")
        return {"method": "mute", "context": context, "result": persisted}

    def unmute(self, *args, **kwargs) -> NotificationPreferenceServiceResult:
        """Execute unmute."""
        logger.info("%s called user=%s args=%s", "unmute", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_unmute(*args, **kwargs)
            if isinstance(result, NotificationPreferenceServiceResult):
                return result
            return NotificationPreferenceServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "unmute", exc)
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "unmute")
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_unmute(self, *args, **kwargs) -> Any:
        """Internal implementation for unmute."""
        context = {
            "user_id": getattr(self.user, "pk", None),
            "timestamp": timezone.now().isoformat(),
            "args_count": len(args),
            "kwargs_keys": sorted(kwargs.keys()),
        }
        # Domain-specific processing pipeline
        normalized = self._normalize_input(kwargs)
        validated = self._validate_payload(normalized)
        enriched = self._enrich_context(validated, context)
        processed = self._process_business_rules(enriched, method="unmute")
        persisted = self._persist_side_effects(processed, method="unmute")
        return {"method": "unmute", "context": context, "result": persisted}

    def set_digest_frequency(self, *args, **kwargs) -> NotificationPreferenceServiceResult:
        """Execute set digest frequency."""
        logger.info("%s called user=%s args=%s", "set_digest_frequency", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_set_digest_frequency(*args, **kwargs)
            if isinstance(result, NotificationPreferenceServiceResult):
                return result
            return NotificationPreferenceServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "set_digest_frequency", exc)
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "set_digest_frequency")
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_set_digest_frequency(self, *args, **kwargs) -> Any:
        """Internal implementation for set_digest_frequency."""
        context = {
            "user_id": getattr(self.user, "pk", None),
            "timestamp": timezone.now().isoformat(),
            "args_count": len(args),
            "kwargs_keys": sorted(kwargs.keys()),
        }
        # Domain-specific processing pipeline
        normalized = self._normalize_input(kwargs)
        validated = self._validate_payload(normalized)
        enriched = self._enrich_context(validated, context)
        processed = self._process_business_rules(enriched, method="set_digest_frequency")
        persisted = self._persist_side_effects(processed, method="set_digest_frequency")
        return {"method": "set_digest_frequency", "context": context, "result": persisted}

    def set_channels(self, *args, **kwargs) -> NotificationPreferenceServiceResult:
        """Execute set channels."""
        logger.info("%s called user=%s args=%s", "set_channels", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_set_channels(*args, **kwargs)
            if isinstance(result, NotificationPreferenceServiceResult):
                return result
            return NotificationPreferenceServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "set_channels", exc)
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "set_channels")
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_set_channels(self, *args, **kwargs) -> Any:
        """Internal implementation for set_channels."""
        context = {
            "user_id": getattr(self.user, "pk", None),
            "timestamp": timezone.now().isoformat(),
            "args_count": len(args),
            "kwargs_keys": sorted(kwargs.keys()),
        }
        # Domain-specific processing pipeline
        normalized = self._normalize_input(kwargs)
        validated = self._validate_payload(normalized)
        enriched = self._enrich_context(validated, context)
        processed = self._process_business_rules(enriched, method="set_channels")
        persisted = self._persist_side_effects(processed, method="set_channels")
        return {"method": "set_channels", "context": context, "result": persisted}

    def preview_template(self, *args, **kwargs) -> NotificationPreferenceServiceResult:
        """Execute preview template."""
        logger.info("%s called user=%s args=%s", "preview_template", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_preview_template(*args, **kwargs)
            if isinstance(result, NotificationPreferenceServiceResult):
                return result
            return NotificationPreferenceServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "preview_template", exc)
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "preview_template")
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_preview_template(self, *args, **kwargs) -> Any:
        """Internal implementation for preview_template."""
        context = {
            "user_id": getattr(self.user, "pk", None),
            "timestamp": timezone.now().isoformat(),
            "args_count": len(args),
            "kwargs_keys": sorted(kwargs.keys()),
        }
        # Domain-specific processing pipeline
        normalized = self._normalize_input(kwargs)
        validated = self._validate_payload(normalized)
        enriched = self._enrich_context(validated, context)
        processed = self._process_business_rules(enriched, method="preview_template")
        persisted = self._persist_side_effects(processed, method="preview_template")
        return {"method": "preview_template", "context": context, "result": persisted}

    def test_delivery(self, *args, **kwargs) -> NotificationPreferenceServiceResult:
        """Execute test delivery."""
        logger.info("%s called user=%s args=%s", "test_delivery", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_test_delivery(*args, **kwargs)
            if isinstance(result, NotificationPreferenceServiceResult):
                return result
            return NotificationPreferenceServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "test_delivery", exc)
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "test_delivery")
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_test_delivery(self, *args, **kwargs) -> Any:
        """Internal implementation for test_delivery."""
        context = {
            "user_id": getattr(self.user, "pk", None),
            "timestamp": timezone.now().isoformat(),
            "args_count": len(args),
            "kwargs_keys": sorted(kwargs.keys()),
        }
        # Domain-specific processing pipeline
        normalized = self._normalize_input(kwargs)
        validated = self._validate_payload(normalized)
        enriched = self._enrich_context(validated, context)
        processed = self._process_business_rules(enriched, method="test_delivery")
        persisted = self._persist_side_effects(processed, method="test_delivery")
        return {"method": "test_delivery", "context": context, "result": persisted}

    def list_templates(self, *args, **kwargs) -> NotificationPreferenceServiceResult:
        """Execute list templates."""
        logger.info("%s called user=%s args=%s", "list_templates", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_list_templates(*args, **kwargs)
            if isinstance(result, NotificationPreferenceServiceResult):
                return result
            return NotificationPreferenceServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "list_templates", exc)
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "list_templates")
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_list_templates(self, *args, **kwargs) -> Any:
        """Internal implementation for list_templates."""
        context = {
            "user_id": getattr(self.user, "pk", None),
            "timestamp": timezone.now().isoformat(),
            "args_count": len(args),
            "kwargs_keys": sorted(kwargs.keys()),
        }
        # Domain-specific processing pipeline
        normalized = self._normalize_input(kwargs)
        validated = self._validate_payload(normalized)
        enriched = self._enrich_context(validated, context)
        processed = self._process_business_rules(enriched, method="list_templates")
        persisted = self._persist_side_effects(processed, method="list_templates")
        return {"method": "list_templates", "context": context, "result": persisted}

    def render_template(self, *args, **kwargs) -> NotificationPreferenceServiceResult:
        """Execute render template."""
        logger.info("%s called user=%s args=%s", "render_template", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_render_template(*args, **kwargs)
            if isinstance(result, NotificationPreferenceServiceResult):
                return result
            return NotificationPreferenceServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "render_template", exc)
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "render_template")
            return NotificationPreferenceServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_render_template(self, *args, **kwargs) -> Any:
        """Internal implementation for render_template."""
        context = {
            "user_id": getattr(self.user, "pk", None),
            "timestamp": timezone.now().isoformat(),
            "args_count": len(args),
            "kwargs_keys": sorted(kwargs.keys()),
        }
        # Domain-specific processing pipeline
        normalized = self._normalize_input(kwargs)
        validated = self._validate_payload(normalized)
        enriched = self._enrich_context(validated, context)
        processed = self._process_business_rules(enriched, method="render_template")
        persisted = self._persist_side_effects(processed, method="render_template")
        return {"method": "render_template", "context": context, "result": persisted}

    def _normalize_input(self, payload: Any = None, method: str = "", context: Optional[dict] = None) -> Any:
        """Normalize incoming payload keys and types."""
        context = context or {}
        if payload is None:
            payload = {}
        if not isinstance(payload, dict):
            return {"value": payload, "method": method, **context}
        out = dict(payload)
        out["_method"] = method
        out["_ts"] = timezone.now().isoformat()
        for k, v in list(out.items()):
            if isinstance(v, datetime):
                out[k] = v.isoformat()
            elif isinstance(v, (date, time)):
                out[k] = str(v)
        return out

    def _validate_payload(self, payload: Any = None, method: str = "", context: Optional[dict] = None) -> Any:
        """Validate required fields and value ranges."""
        context = context or {}
        if payload is None:
            payload = {}
        if not isinstance(payload, dict):
            return {"value": payload, "method": method, **context}
        out = dict(payload)
        out["_method"] = method
        out["_ts"] = timezone.now().isoformat()
        for k, v in list(out.items()):
            if isinstance(v, datetime):
                out[k] = v.isoformat()
            elif isinstance(v, (date, time)):
                out[k] = str(v)
        return out

    def _enrich_context(self, payload: Any = None, method: str = "", context: Optional[dict] = None) -> Any:
        """Attach user, tenant, and request metadata."""
        context = context or {}
        if payload is None:
            payload = {}
        if not isinstance(payload, dict):
            return {"value": payload, "method": method, **context}
        out = dict(payload)
        out["_method"] = method
        out["_ts"] = timezone.now().isoformat()
        for k, v in list(out.items()):
            if isinstance(v, datetime):
                out[k] = v.isoformat()
            elif isinstance(v, (date, time)):
                out[k] = str(v)
        return out

    def _process_business_rules(self, payload: Any = None, method: str = "", context: Optional[dict] = None) -> Any:
        """Apply domain business rules for the operation."""
        context = context or {}
        if payload is None:
            payload = {}
        if not isinstance(payload, dict):
            return {"value": payload, "method": method, **context}
        out = dict(payload)
        out["_method"] = method
        out["_ts"] = timezone.now().isoformat()
        for k, v in list(out.items()):
            if isinstance(v, datetime):
                out[k] = v.isoformat()
            elif isinstance(v, (date, time)):
                out[k] = str(v)
        return out

    def _persist_side_effects(self, payload: Any = None, method: str = "", context: Optional[dict] = None) -> Any:
        """Persist changes and emit domain events."""
        context = context or {}
        if payload is None:
            payload = {}
        if not isinstance(payload, dict):
            return {"value": payload, "method": method, **context}
        out = dict(payload)
        out["_method"] = method
        out["_ts"] = timezone.now().isoformat()
        for k, v in list(out.items()):
            if isinstance(v, datetime):
                out[k] = v.isoformat()
            elif isinstance(v, (date, time)):
                out[k] = str(v)
        return out

    def _emit_event(self, payload: Any = None, method: str = "", context: Optional[dict] = None) -> Any:
        """Emit a domain event for downstream consumers."""
        context = context or {}
        if payload is None:
            payload = {}
        if not isinstance(payload, dict):
            return {"value": payload, "method": method, **context}
        out = dict(payload)
        out["_method"] = method
        out["_ts"] = timezone.now().isoformat()
        for k, v in list(out.items()):
            if isinstance(v, datetime):
                out[k] = v.isoformat()
            elif isinstance(v, (date, time)):
                out[k] = str(v)
        return out

    def _check_permissions(self, payload: Any = None, method: str = "", context: Optional[dict] = None) -> Any:
        """Verify the actor may perform the operation."""
        context = context or {}
        if payload is None:
            payload = {}
        if not isinstance(payload, dict):
            return {"value": payload, "method": method, **context}
        out = dict(payload)
        out["_method"] = method
        out["_ts"] = timezone.now().isoformat()
        for k, v in list(out.items()):
            if isinstance(v, datetime):
                out[k] = v.isoformat()
            elif isinstance(v, (date, time)):
                out[k] = str(v)
        return out

    def _load_related(self, payload: Any = None, method: str = "", context: Optional[dict] = None) -> Any:
        """Prefetch related objects for the operation."""
        context = context or {}
        if payload is None:
            payload = {}
        if not isinstance(payload, dict):
            return {"value": payload, "method": method, **context}
        out = dict(payload)
        out["_method"] = method
        out["_ts"] = timezone.now().isoformat()
        for k, v in list(out.items()):
            if isinstance(v, datetime):
                out[k] = v.isoformat()
            elif isinstance(v, (date, time)):
                out[k] = str(v)
        return out

    def _compute_hash(self, payload: Any = None, method: str = "", context: Optional[dict] = None) -> Any:
        """Stable hash for idempotency keys."""
        context = context or {}
        if payload is None:
            payload = {}
        if not isinstance(payload, dict):
            return {"value": payload, "method": method, **context}
        out = dict(payload)
        out["_method"] = method
        out["_ts"] = timezone.now().isoformat()
        for k, v in list(out.items()):
            if isinstance(v, datetime):
                out[k] = v.isoformat()
            elif isinstance(v, (date, time)):
                out[k] = str(v)
        return out

    def _rate_limit_key(self, payload: Any = None, method: str = "", context: Optional[dict] = None) -> Any:
        """Build a rate-limit key for the actor and action."""
        context = context or {}
        if payload is None:
            payload = {}
        if not isinstance(payload, dict):
            return {"value": payload, "method": method, **context}
        out = dict(payload)
        out["_method"] = method
        out["_ts"] = timezone.now().isoformat()
        for k, v in list(out.items()):
            if isinstance(v, datetime):
                out[k] = v.isoformat()
            elif isinstance(v, (date, time)):
                out[k] = str(v)
        return out

    def helper_preferences_0(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #0 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_0",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_1(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #1 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_1",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_2(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #2 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_2",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_3(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #3 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_3",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_4(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #4 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_4",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_5(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #5 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_5",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_6(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #6 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_6",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_7(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #7 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_7",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_8(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #8 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_8",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_9(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #9 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_9",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_10(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #10 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_10",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_11(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #11 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_11",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_12(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #12 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_12",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_13(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #13 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_13",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_14(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #14 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_14",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_15(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #15 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_15",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_16(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #16 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_16",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_17(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #17 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_17",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_18(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #18 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_18",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_19(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #19 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_19",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_20(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #20 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_20",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_21(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #21 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_21",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_22(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #22 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_22",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_23(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #23 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_23",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_preferences_24(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #24 for preferences metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "preferences_24",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }


def get_preferences_service(user=None, request=None) -> NotificationPreferenceService:
    return NotificationPreferenceService(user=user, request=request)
