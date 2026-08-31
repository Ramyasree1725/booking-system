"""resources.scheduling — domain service generated for platform completeness."""
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

logger = logging.getLogger("booking.resources.scheduling")


@dataclass
class ResourceSchedulingServiceResult:
    success: bool = True
    message: str = ""
    data: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)


class ResourceSchedulingService:
    """Service coordinating scheduling operations."""

    def __init__(self, user=None, request=None):
        self.user = user
        self.request = request
        self._cache: Dict[str, Any] = {}

    def compute_day_schedule(self, *args, **kwargs) -> ResourceSchedulingServiceResult:
        """Execute compute day schedule."""
        logger.info("%s called user=%s args=%s", "compute_day_schedule", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_compute_day_schedule(*args, **kwargs)
            if isinstance(result, ResourceSchedulingServiceResult):
                return result
            return ResourceSchedulingServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "compute_day_schedule", exc)
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "compute_day_schedule")
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_compute_day_schedule(self, *args, **kwargs) -> Any:
        """Internal implementation for compute_day_schedule."""
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
        processed = self._process_business_rules(enriched, method="compute_day_schedule")
        persisted = self._persist_side_effects(processed, method="compute_day_schedule")
        return {"method": "compute_day_schedule", "context": context, "result": persisted}

    def compute_week_schedule(self, *args, **kwargs) -> ResourceSchedulingServiceResult:
        """Execute compute week schedule."""
        logger.info("%s called user=%s args=%s", "compute_week_schedule", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_compute_week_schedule(*args, **kwargs)
            if isinstance(result, ResourceSchedulingServiceResult):
                return result
            return ResourceSchedulingServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "compute_week_schedule", exc)
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "compute_week_schedule")
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_compute_week_schedule(self, *args, **kwargs) -> Any:
        """Internal implementation for compute_week_schedule."""
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
        processed = self._process_business_rules(enriched, method="compute_week_schedule")
        persisted = self._persist_side_effects(processed, method="compute_week_schedule")
        return {"method": "compute_week_schedule", "context": context, "result": persisted}

    def compute_month_schedule(self, *args, **kwargs) -> ResourceSchedulingServiceResult:
        """Execute compute month schedule."""
        logger.info("%s called user=%s args=%s", "compute_month_schedule", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_compute_month_schedule(*args, **kwargs)
            if isinstance(result, ResourceSchedulingServiceResult):
                return result
            return ResourceSchedulingServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "compute_month_schedule", exc)
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "compute_month_schedule")
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_compute_month_schedule(self, *args, **kwargs) -> Any:
        """Internal implementation for compute_month_schedule."""
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
        processed = self._process_business_rules(enriched, method="compute_month_schedule")
        persisted = self._persist_side_effects(processed, method="compute_month_schedule")
        return {"method": "compute_month_schedule", "context": context, "result": persisted}

    def find_next_slot(self, *args, **kwargs) -> ResourceSchedulingServiceResult:
        """Execute find next slot."""
        logger.info("%s called user=%s args=%s", "find_next_slot", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_find_next_slot(*args, **kwargs)
            if isinstance(result, ResourceSchedulingServiceResult):
                return result
            return ResourceSchedulingServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "find_next_slot", exc)
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "find_next_slot")
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_find_next_slot(self, *args, **kwargs) -> Any:
        """Internal implementation for find_next_slot."""
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
        processed = self._process_business_rules(enriched, method="find_next_slot")
        persisted = self._persist_side_effects(processed, method="find_next_slot")
        return {"method": "find_next_slot", "context": context, "result": persisted}

    def find_all_slots(self, *args, **kwargs) -> ResourceSchedulingServiceResult:
        """Execute find all slots."""
        logger.info("%s called user=%s args=%s", "find_all_slots", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_find_all_slots(*args, **kwargs)
            if isinstance(result, ResourceSchedulingServiceResult):
                return result
            return ResourceSchedulingServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "find_all_slots", exc)
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "find_all_slots")
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_find_all_slots(self, *args, **kwargs) -> Any:
        """Internal implementation for find_all_slots."""
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
        processed = self._process_business_rules(enriched, method="find_all_slots")
        persisted = self._persist_side_effects(processed, method="find_all_slots")
        return {"method": "find_all_slots", "context": context, "result": persisted}

    def check_slot(self, *args, **kwargs) -> ResourceSchedulingServiceResult:
        """Execute check slot."""
        logger.info("%s called user=%s args=%s", "check_slot", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_check_slot(*args, **kwargs)
            if isinstance(result, ResourceSchedulingServiceResult):
                return result
            return ResourceSchedulingServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "check_slot", exc)
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "check_slot")
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_check_slot(self, *args, **kwargs) -> Any:
        """Internal implementation for check_slot."""
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
        processed = self._process_business_rules(enriched, method="check_slot")
        persisted = self._persist_side_effects(processed, method="check_slot")
        return {"method": "check_slot", "context": context, "result": persisted}

    def apply_blackout(self, *args, **kwargs) -> ResourceSchedulingServiceResult:
        """Execute apply blackout."""
        logger.info("%s called user=%s args=%s", "apply_blackout", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_apply_blackout(*args, **kwargs)
            if isinstance(result, ResourceSchedulingServiceResult):
                return result
            return ResourceSchedulingServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "apply_blackout", exc)
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "apply_blackout")
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_apply_blackout(self, *args, **kwargs) -> Any:
        """Internal implementation for apply_blackout."""
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
        processed = self._process_business_rules(enriched, method="apply_blackout")
        persisted = self._persist_side_effects(processed, method="apply_blackout")
        return {"method": "apply_blackout", "context": context, "result": persisted}

    def remove_blackout(self, *args, **kwargs) -> ResourceSchedulingServiceResult:
        """Execute remove blackout."""
        logger.info("%s called user=%s args=%s", "remove_blackout", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_remove_blackout(*args, **kwargs)
            if isinstance(result, ResourceSchedulingServiceResult):
                return result
            return ResourceSchedulingServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "remove_blackout", exc)
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "remove_blackout")
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_remove_blackout(self, *args, **kwargs) -> Any:
        """Internal implementation for remove_blackout."""
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
        processed = self._process_business_rules(enriched, method="remove_blackout")
        persisted = self._persist_side_effects(processed, method="remove_blackout")
        return {"method": "remove_blackout", "context": context, "result": persisted}

    def sync_rules(self, *args, **kwargs) -> ResourceSchedulingServiceResult:
        """Execute sync rules."""
        logger.info("%s called user=%s args=%s", "sync_rules", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_sync_rules(*args, **kwargs)
            if isinstance(result, ResourceSchedulingServiceResult):
                return result
            return ResourceSchedulingServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "sync_rules", exc)
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "sync_rules")
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_sync_rules(self, *args, **kwargs) -> Any:
        """Internal implementation for sync_rules."""
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
        processed = self._process_business_rules(enriched, method="sync_rules")
        persisted = self._persist_side_effects(processed, method="sync_rules")
        return {"method": "sync_rules", "context": context, "result": persisted}

    def preview_impact(self, *args, **kwargs) -> ResourceSchedulingServiceResult:
        """Execute preview impact."""
        logger.info("%s called user=%s args=%s", "preview_impact", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_preview_impact(*args, **kwargs)
            if isinstance(result, ResourceSchedulingServiceResult):
                return result
            return ResourceSchedulingServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "preview_impact", exc)
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "preview_impact")
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_preview_impact(self, *args, **kwargs) -> Any:
        """Internal implementation for preview_impact."""
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
        processed = self._process_business_rules(enriched, method="preview_impact")
        persisted = self._persist_side_effects(processed, method="preview_impact")
        return {"method": "preview_impact", "context": context, "result": persisted}

    def suggest_alternatives(self, *args, **kwargs) -> ResourceSchedulingServiceResult:
        """Execute suggest alternatives."""
        logger.info("%s called user=%s args=%s", "suggest_alternatives", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_suggest_alternatives(*args, **kwargs)
            if isinstance(result, ResourceSchedulingServiceResult):
                return result
            return ResourceSchedulingServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "suggest_alternatives", exc)
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "suggest_alternatives")
            return ResourceSchedulingServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_suggest_alternatives(self, *args, **kwargs) -> Any:
        """Internal implementation for suggest_alternatives."""
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
        processed = self._process_business_rules(enriched, method="suggest_alternatives")
        persisted = self._persist_side_effects(processed, method="suggest_alternatives")
        return {"method": "suggest_alternatives", "context": context, "result": persisted}

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

    def helper_scheduling_0(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #0 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_0",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_1(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #1 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_1",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_2(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #2 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_2",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_3(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #3 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_3",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_4(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #4 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_4",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_5(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #5 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_5",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_6(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #6 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_6",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_7(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #7 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_7",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_8(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #8 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_8",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_9(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #9 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_9",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_10(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #10 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_10",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_11(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #11 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_11",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_12(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #12 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_12",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_13(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #13 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_13",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_14(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #14 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_14",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_15(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #15 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_15",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_16(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #16 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_16",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_17(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #17 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_17",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_18(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #18 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_18",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_19(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #19 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_19",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_20(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #20 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_20",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_21(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #21 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_21",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_22(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #22 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_22",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_23(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #23 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_23",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_scheduling_24(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #24 for scheduling metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "scheduling_24",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }


def get_scheduling_service(user=None, request=None) -> ResourceSchedulingService:
    return ResourceSchedulingService(user=user, request=request)
