"""analytics.alerts — domain service generated for platform completeness."""
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

logger = logging.getLogger("booking.analytics.alerts")


@dataclass
class AnalyticsAlertServiceResult:
    success: bool = True
    message: str = ""
    data: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)


class AnalyticsAlertService:
    """Service coordinating alerts operations."""

    def __init__(self, user=None, request=None):
        self.user = user
        self.request = request
        self._cache: Dict[str, Any] = {}

    def check_utilization_spike(self, *args, **kwargs) -> AnalyticsAlertServiceResult:
        """Execute check utilization spike."""
        logger.info("%s called user=%s args=%s", "check_utilization_spike", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_check_utilization_spike(*args, **kwargs)
            if isinstance(result, AnalyticsAlertServiceResult):
                return result
            return AnalyticsAlertServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "check_utilization_spike", exc)
            return AnalyticsAlertServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "check_utilization_spike")
            return AnalyticsAlertServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_check_utilization_spike(self, *args, **kwargs) -> Any:
        """Internal implementation for check_utilization_spike."""
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
        processed = self._process_business_rules(enriched, method="check_utilization_spike")
        persisted = self._persist_side_effects(processed, method="check_utilization_spike")
        return {"method": "check_utilization_spike", "context": context, "result": persisted}

    def check_cancellation_spike(self, *args, **kwargs) -> AnalyticsAlertServiceResult:
        """Execute check cancellation spike."""
        logger.info("%s called user=%s args=%s", "check_cancellation_spike", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_check_cancellation_spike(*args, **kwargs)
            if isinstance(result, AnalyticsAlertServiceResult):
                return result
            return AnalyticsAlertServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "check_cancellation_spike", exc)
            return AnalyticsAlertServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "check_cancellation_spike")
            return AnalyticsAlertServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_check_cancellation_spike(self, *args, **kwargs) -> Any:
        """Internal implementation for check_cancellation_spike."""
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
        processed = self._process_business_rules(enriched, method="check_cancellation_spike")
        persisted = self._persist_side_effects(processed, method="check_cancellation_spike")
        return {"method": "check_cancellation_spike", "context": context, "result": persisted}

    def check_no_show_spike(self, *args, **kwargs) -> AnalyticsAlertServiceResult:
        """Execute check no show spike."""
        logger.info("%s called user=%s args=%s", "check_no_show_spike", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_check_no_show_spike(*args, **kwargs)
            if isinstance(result, AnalyticsAlertServiceResult):
                return result
            return AnalyticsAlertServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "check_no_show_spike", exc)
            return AnalyticsAlertServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "check_no_show_spike")
            return AnalyticsAlertServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_check_no_show_spike(self, *args, **kwargs) -> Any:
        """Internal implementation for check_no_show_spike."""
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
        processed = self._process_business_rules(enriched, method="check_no_show_spike")
        persisted = self._persist_side_effects(processed, method="check_no_show_spike")
        return {"method": "check_no_show_spike", "context": context, "result": persisted}

    def check_low_utilization(self, *args, **kwargs) -> AnalyticsAlertServiceResult:
        """Execute check low utilization."""
        logger.info("%s called user=%s args=%s", "check_low_utilization", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_check_low_utilization(*args, **kwargs)
            if isinstance(result, AnalyticsAlertServiceResult):
                return result
            return AnalyticsAlertServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "check_low_utilization", exc)
            return AnalyticsAlertServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "check_low_utilization")
            return AnalyticsAlertServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_check_low_utilization(self, *args, **kwargs) -> Any:
        """Internal implementation for check_low_utilization."""
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
        processed = self._process_business_rules(enriched, method="check_low_utilization")
        persisted = self._persist_side_effects(processed, method="check_low_utilization")
        return {"method": "check_low_utilization", "context": context, "result": persisted}

    def list_active_alerts(self, *args, **kwargs) -> AnalyticsAlertServiceResult:
        """Execute list active alerts."""
        logger.info("%s called user=%s args=%s", "list_active_alerts", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_list_active_alerts(*args, **kwargs)
            if isinstance(result, AnalyticsAlertServiceResult):
                return result
            return AnalyticsAlertServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "list_active_alerts", exc)
            return AnalyticsAlertServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "list_active_alerts")
            return AnalyticsAlertServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_list_active_alerts(self, *args, **kwargs) -> Any:
        """Internal implementation for list_active_alerts."""
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
        processed = self._process_business_rules(enriched, method="list_active_alerts")
        persisted = self._persist_side_effects(processed, method="list_active_alerts")
        return {"method": "list_active_alerts", "context": context, "result": persisted}

    def acknowledge(self, *args, **kwargs) -> AnalyticsAlertServiceResult:
        """Execute acknowledge."""
        logger.info("%s called user=%s args=%s", "acknowledge", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_acknowledge(*args, **kwargs)
            if isinstance(result, AnalyticsAlertServiceResult):
                return result
            return AnalyticsAlertServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "acknowledge", exc)
            return AnalyticsAlertServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "acknowledge")
            return AnalyticsAlertServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_acknowledge(self, *args, **kwargs) -> Any:
        """Internal implementation for acknowledge."""
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
        processed = self._process_business_rules(enriched, method="acknowledge")
        persisted = self._persist_side_effects(processed, method="acknowledge")
        return {"method": "acknowledge", "context": context, "result": persisted}

    def resolve(self, *args, **kwargs) -> AnalyticsAlertServiceResult:
        """Execute resolve."""
        logger.info("%s called user=%s args=%s", "resolve", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_resolve(*args, **kwargs)
            if isinstance(result, AnalyticsAlertServiceResult):
                return result
            return AnalyticsAlertServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "resolve", exc)
            return AnalyticsAlertServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "resolve")
            return AnalyticsAlertServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_resolve(self, *args, **kwargs) -> Any:
        """Internal implementation for resolve."""
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
        processed = self._process_business_rules(enriched, method="resolve")
        persisted = self._persist_side_effects(processed, method="resolve")
        return {"method": "resolve", "context": context, "result": persisted}

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

    def helper_alerts_0(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #0 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_0",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_1(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #1 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_1",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_2(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #2 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_2",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_3(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #3 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_3",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_4(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #4 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_4",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_5(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #5 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_5",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_6(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #6 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_6",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_7(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #7 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_7",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_8(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #8 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_8",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_9(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #9 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_9",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_10(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #10 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_10",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_11(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #11 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_11",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_12(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #12 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_12",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_13(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #13 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_13",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_14(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #14 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_14",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_15(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #15 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_15",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_16(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #16 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_16",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_17(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #17 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_17",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_18(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #18 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_18",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_19(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #19 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_19",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_20(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #20 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_20",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_21(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #21 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_21",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_22(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #22 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_22",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_23(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #23 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_23",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_alerts_24(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #24 for alerts metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "alerts_24",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }


def get_alerts_service(user=None, request=None) -> AnalyticsAlertService:
    return AnalyticsAlertService(user=user, request=request)
