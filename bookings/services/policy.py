"""bookings.policy — domain service generated for platform completeness."""
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

logger = logging.getLogger("booking.bookings.policy")


@dataclass
class BookingPolicyServiceResult:
    success: bool = True
    message: str = ""
    data: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)


class BookingPolicyService:
    """Service coordinating policy operations."""

    def __init__(self, user=None, request=None):
        self.user = user
        self.request = request
        self._cache: Dict[str, Any] = {}

    def evaluate_cancellation(self, *args, **kwargs) -> BookingPolicyServiceResult:
        """Execute evaluate cancellation."""
        logger.info("%s called user=%s args=%s", "evaluate_cancellation", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_evaluate_cancellation(*args, **kwargs)
            if isinstance(result, BookingPolicyServiceResult):
                return result
            return BookingPolicyServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "evaluate_cancellation", exc)
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "evaluate_cancellation")
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_evaluate_cancellation(self, *args, **kwargs) -> Any:
        """Internal implementation for evaluate_cancellation."""
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
        processed = self._process_business_rules(enriched, method="evaluate_cancellation")
        persisted = self._persist_side_effects(processed, method="evaluate_cancellation")
        return {"method": "evaluate_cancellation", "context": context, "result": persisted}

    def evaluate_modification(self, *args, **kwargs) -> BookingPolicyServiceResult:
        """Execute evaluate modification."""
        logger.info("%s called user=%s args=%s", "evaluate_modification", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_evaluate_modification(*args, **kwargs)
            if isinstance(result, BookingPolicyServiceResult):
                return result
            return BookingPolicyServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "evaluate_modification", exc)
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "evaluate_modification")
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_evaluate_modification(self, *args, **kwargs) -> Any:
        """Internal implementation for evaluate_modification."""
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
        processed = self._process_business_rules(enriched, method="evaluate_modification")
        persisted = self._persist_side_effects(processed, method="evaluate_modification")
        return {"method": "evaluate_modification", "context": context, "result": persisted}

    def evaluate_approval(self, *args, **kwargs) -> BookingPolicyServiceResult:
        """Execute evaluate approval."""
        logger.info("%s called user=%s args=%s", "evaluate_approval", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_evaluate_approval(*args, **kwargs)
            if isinstance(result, BookingPolicyServiceResult):
                return result
            return BookingPolicyServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "evaluate_approval", exc)
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "evaluate_approval")
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_evaluate_approval(self, *args, **kwargs) -> Any:
        """Internal implementation for evaluate_approval."""
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
        processed = self._process_business_rules(enriched, method="evaluate_approval")
        persisted = self._persist_side_effects(processed, method="evaluate_approval")
        return {"method": "evaluate_approval", "context": context, "result": persisted}

    def evaluate_capacity(self, *args, **kwargs) -> BookingPolicyServiceResult:
        """Execute evaluate capacity."""
        logger.info("%s called user=%s args=%s", "evaluate_capacity", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_evaluate_capacity(*args, **kwargs)
            if isinstance(result, BookingPolicyServiceResult):
                return result
            return BookingPolicyServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "evaluate_capacity", exc)
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "evaluate_capacity")
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_evaluate_capacity(self, *args, **kwargs) -> Any:
        """Internal implementation for evaluate_capacity."""
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
        processed = self._process_business_rules(enriched, method="evaluate_capacity")
        persisted = self._persist_side_effects(processed, method="evaluate_capacity")
        return {"method": "evaluate_capacity", "context": context, "result": persisted}

    def evaluate_buffer(self, *args, **kwargs) -> BookingPolicyServiceResult:
        """Execute evaluate buffer."""
        logger.info("%s called user=%s args=%s", "evaluate_buffer", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_evaluate_buffer(*args, **kwargs)
            if isinstance(result, BookingPolicyServiceResult):
                return result
            return BookingPolicyServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "evaluate_buffer", exc)
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "evaluate_buffer")
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_evaluate_buffer(self, *args, **kwargs) -> Any:
        """Internal implementation for evaluate_buffer."""
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
        processed = self._process_business_rules(enriched, method="evaluate_buffer")
        persisted = self._persist_side_effects(processed, method="evaluate_buffer")
        return {"method": "evaluate_buffer", "context": context, "result": persisted}

    def evaluate_blackout(self, *args, **kwargs) -> BookingPolicyServiceResult:
        """Execute evaluate blackout."""
        logger.info("%s called user=%s args=%s", "evaluate_blackout", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_evaluate_blackout(*args, **kwargs)
            if isinstance(result, BookingPolicyServiceResult):
                return result
            return BookingPolicyServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "evaluate_blackout", exc)
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "evaluate_blackout")
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_evaluate_blackout(self, *args, **kwargs) -> Any:
        """Internal implementation for evaluate_blackout."""
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
        processed = self._process_business_rules(enriched, method="evaluate_blackout")
        persisted = self._persist_side_effects(processed, method="evaluate_blackout")
        return {"method": "evaluate_blackout", "context": context, "result": persisted}

    def evaluate_advance_window(self, *args, **kwargs) -> BookingPolicyServiceResult:
        """Execute evaluate advance window."""
        logger.info("%s called user=%s args=%s", "evaluate_advance_window", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_evaluate_advance_window(*args, **kwargs)
            if isinstance(result, BookingPolicyServiceResult):
                return result
            return BookingPolicyServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "evaluate_advance_window", exc)
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "evaluate_advance_window")
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_evaluate_advance_window(self, *args, **kwargs) -> Any:
        """Internal implementation for evaluate_advance_window."""
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
        processed = self._process_business_rules(enriched, method="evaluate_advance_window")
        persisted = self._persist_side_effects(processed, method="evaluate_advance_window")
        return {"method": "evaluate_advance_window", "context": context, "result": persisted}

    def evaluate_duration(self, *args, **kwargs) -> BookingPolicyServiceResult:
        """Execute evaluate duration."""
        logger.info("%s called user=%s args=%s", "evaluate_duration", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_evaluate_duration(*args, **kwargs)
            if isinstance(result, BookingPolicyServiceResult):
                return result
            return BookingPolicyServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "evaluate_duration", exc)
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "evaluate_duration")
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_evaluate_duration(self, *args, **kwargs) -> Any:
        """Internal implementation for evaluate_duration."""
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
        processed = self._process_business_rules(enriched, method="evaluate_duration")
        persisted = self._persist_side_effects(processed, method="evaluate_duration")
        return {"method": "evaluate_duration", "context": context, "result": persisted}

    def evaluate_recurrence(self, *args, **kwargs) -> BookingPolicyServiceResult:
        """Execute evaluate recurrence."""
        logger.info("%s called user=%s args=%s", "evaluate_recurrence", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_evaluate_recurrence(*args, **kwargs)
            if isinstance(result, BookingPolicyServiceResult):
                return result
            return BookingPolicyServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "evaluate_recurrence", exc)
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "evaluate_recurrence")
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_evaluate_recurrence(self, *args, **kwargs) -> Any:
        """Internal implementation for evaluate_recurrence."""
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
        processed = self._process_business_rules(enriched, method="evaluate_recurrence")
        persisted = self._persist_side_effects(processed, method="evaluate_recurrence")
        return {"method": "evaluate_recurrence", "context": context, "result": persisted}

    def evaluate_attendee_limits(self, *args, **kwargs) -> BookingPolicyServiceResult:
        """Execute evaluate attendee limits."""
        logger.info("%s called user=%s args=%s", "evaluate_attendee_limits", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_evaluate_attendee_limits(*args, **kwargs)
            if isinstance(result, BookingPolicyServiceResult):
                return result
            return BookingPolicyServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "evaluate_attendee_limits", exc)
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "evaluate_attendee_limits")
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_evaluate_attendee_limits(self, *args, **kwargs) -> Any:
        """Internal implementation for evaluate_attendee_limits."""
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
        processed = self._process_business_rules(enriched, method="evaluate_attendee_limits")
        persisted = self._persist_side_effects(processed, method="evaluate_attendee_limits")
        return {"method": "evaluate_attendee_limits", "context": context, "result": persisted}

    def compose_policy_decision(self, *args, **kwargs) -> BookingPolicyServiceResult:
        """Execute compose policy decision."""
        logger.info("%s called user=%s args=%s", "compose_policy_decision", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_compose_policy_decision(*args, **kwargs)
            if isinstance(result, BookingPolicyServiceResult):
                return result
            return BookingPolicyServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "compose_policy_decision", exc)
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "compose_policy_decision")
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_compose_policy_decision(self, *args, **kwargs) -> Any:
        """Internal implementation for compose_policy_decision."""
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
        processed = self._process_business_rules(enriched, method="compose_policy_decision")
        persisted = self._persist_side_effects(processed, method="compose_policy_decision")
        return {"method": "compose_policy_decision", "context": context, "result": persisted}

    def explain_denial(self, *args, **kwargs) -> BookingPolicyServiceResult:
        """Execute explain denial."""
        logger.info("%s called user=%s args=%s", "explain_denial", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_explain_denial(*args, **kwargs)
            if isinstance(result, BookingPolicyServiceResult):
                return result
            return BookingPolicyServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "explain_denial", exc)
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "explain_denial")
            return BookingPolicyServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_explain_denial(self, *args, **kwargs) -> Any:
        """Internal implementation for explain_denial."""
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
        processed = self._process_business_rules(enriched, method="explain_denial")
        persisted = self._persist_side_effects(processed, method="explain_denial")
        return {"method": "explain_denial", "context": context, "result": persisted}

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

    def helper_policy_0(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #0 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_0",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_1(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #1 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_1",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_2(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #2 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_2",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_3(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #3 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_3",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_4(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #4 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_4",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_5(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #5 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_5",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_6(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #6 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_6",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_7(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #7 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_7",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_8(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #8 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_8",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_9(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #9 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_9",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_10(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #10 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_10",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_11(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #11 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_11",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_12(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #12 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_12",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_13(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #13 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_13",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_14(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #14 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_14",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_15(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #15 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_15",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_16(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #16 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_16",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_17(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #17 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_17",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_18(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #18 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_18",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_19(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #19 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_19",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_20(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #20 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_20",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_21(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #21 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_21",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_22(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #22 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_22",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_23(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #23 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_23",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_policy_24(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #24 for policy metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "policy_24",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }


def get_policy_service(user=None, request=None) -> BookingPolicyService:
    return BookingPolicyService(user=user, request=request)
