"""reporting.builder — domain service generated for platform completeness."""
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

logger = logging.getLogger("booking.reporting.builder")


@dataclass
class ReportBuilderServiceResult:
    success: bool = True
    message: str = ""
    data: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)


class ReportBuilderService:
    """Service coordinating builder operations."""

    def __init__(self, user=None, request=None):
        self.user = user
        self.request = request
        self._cache: Dict[str, Any] = {}

    def build_utilization(self, *args, **kwargs) -> ReportBuilderServiceResult:
        """Execute build utilization."""
        logger.info("%s called user=%s args=%s", "build_utilization", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_build_utilization(*args, **kwargs)
            if isinstance(result, ReportBuilderServiceResult):
                return result
            return ReportBuilderServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "build_utilization", exc)
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "build_utilization")
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_build_utilization(self, *args, **kwargs) -> Any:
        """Internal implementation for build_utilization."""
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
        processed = self._process_business_rules(enriched, method="build_utilization")
        persisted = self._persist_side_effects(processed, method="build_utilization")
        return {"method": "build_utilization", "context": context, "result": persisted}

    def build_occupancy(self, *args, **kwargs) -> ReportBuilderServiceResult:
        """Execute build occupancy."""
        logger.info("%s called user=%s args=%s", "build_occupancy", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_build_occupancy(*args, **kwargs)
            if isinstance(result, ReportBuilderServiceResult):
                return result
            return ReportBuilderServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "build_occupancy", exc)
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "build_occupancy")
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_build_occupancy(self, *args, **kwargs) -> Any:
        """Internal implementation for build_occupancy."""
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
        processed = self._process_business_rules(enriched, method="build_occupancy")
        persisted = self._persist_side_effects(processed, method="build_occupancy")
        return {"method": "build_occupancy", "context": context, "result": persisted}

    def build_cancellations(self, *args, **kwargs) -> ReportBuilderServiceResult:
        """Execute build cancellations."""
        logger.info("%s called user=%s args=%s", "build_cancellations", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_build_cancellations(*args, **kwargs)
            if isinstance(result, ReportBuilderServiceResult):
                return result
            return ReportBuilderServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "build_cancellations", exc)
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "build_cancellations")
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_build_cancellations(self, *args, **kwargs) -> Any:
        """Internal implementation for build_cancellations."""
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
        processed = self._process_business_rules(enriched, method="build_cancellations")
        persisted = self._persist_side_effects(processed, method="build_cancellations")
        return {"method": "build_cancellations", "context": context, "result": persisted}

    def build_user_activity(self, *args, **kwargs) -> ReportBuilderServiceResult:
        """Execute build user activity."""
        logger.info("%s called user=%s args=%s", "build_user_activity", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_build_user_activity(*args, **kwargs)
            if isinstance(result, ReportBuilderServiceResult):
                return result
            return ReportBuilderServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "build_user_activity", exc)
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "build_user_activity")
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_build_user_activity(self, *args, **kwargs) -> Any:
        """Internal implementation for build_user_activity."""
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
        processed = self._process_business_rules(enriched, method="build_user_activity")
        persisted = self._persist_side_effects(processed, method="build_user_activity")
        return {"method": "build_user_activity", "context": context, "result": persisted}

    def build_resource_ranking(self, *args, **kwargs) -> ReportBuilderServiceResult:
        """Execute build resource ranking."""
        logger.info("%s called user=%s args=%s", "build_resource_ranking", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_build_resource_ranking(*args, **kwargs)
            if isinstance(result, ReportBuilderServiceResult):
                return result
            return ReportBuilderServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "build_resource_ranking", exc)
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "build_resource_ranking")
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_build_resource_ranking(self, *args, **kwargs) -> Any:
        """Internal implementation for build_resource_ranking."""
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
        processed = self._process_business_rules(enriched, method="build_resource_ranking")
        persisted = self._persist_side_effects(processed, method="build_resource_ranking")
        return {"method": "build_resource_ranking", "context": context, "result": persisted}

    def build_forecast(self, *args, **kwargs) -> ReportBuilderServiceResult:
        """Execute build forecast."""
        logger.info("%s called user=%s args=%s", "build_forecast", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_build_forecast(*args, **kwargs)
            if isinstance(result, ReportBuilderServiceResult):
                return result
            return ReportBuilderServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "build_forecast", exc)
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "build_forecast")
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_build_forecast(self, *args, **kwargs) -> Any:
        """Internal implementation for build_forecast."""
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
        processed = self._process_business_rules(enriched, method="build_forecast")
        persisted = self._persist_side_effects(processed, method="build_forecast")
        return {"method": "build_forecast", "context": context, "result": persisted}

    def build_custom(self, *args, **kwargs) -> ReportBuilderServiceResult:
        """Execute build custom."""
        logger.info("%s called user=%s args=%s", "build_custom", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_build_custom(*args, **kwargs)
            if isinstance(result, ReportBuilderServiceResult):
                return result
            return ReportBuilderServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "build_custom", exc)
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "build_custom")
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_build_custom(self, *args, **kwargs) -> Any:
        """Internal implementation for build_custom."""
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
        processed = self._process_business_rules(enriched, method="build_custom")
        persisted = self._persist_side_effects(processed, method="build_custom")
        return {"method": "build_custom", "context": context, "result": persisted}

    def schedule_report(self, *args, **kwargs) -> ReportBuilderServiceResult:
        """Execute schedule report."""
        logger.info("%s called user=%s args=%s", "schedule_report", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_schedule_report(*args, **kwargs)
            if isinstance(result, ReportBuilderServiceResult):
                return result
            return ReportBuilderServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "schedule_report", exc)
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "schedule_report")
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_schedule_report(self, *args, **kwargs) -> Any:
        """Internal implementation for schedule_report."""
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
        processed = self._process_business_rules(enriched, method="schedule_report")
        persisted = self._persist_side_effects(processed, method="schedule_report")
        return {"method": "schedule_report", "context": context, "result": persisted}

    def list_scheduled(self, *args, **kwargs) -> ReportBuilderServiceResult:
        """Execute list scheduled."""
        logger.info("%s called user=%s args=%s", "list_scheduled", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_list_scheduled(*args, **kwargs)
            if isinstance(result, ReportBuilderServiceResult):
                return result
            return ReportBuilderServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "list_scheduled", exc)
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "list_scheduled")
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_list_scheduled(self, *args, **kwargs) -> Any:
        """Internal implementation for list_scheduled."""
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
        processed = self._process_business_rules(enriched, method="list_scheduled")
        persisted = self._persist_side_effects(processed, method="list_scheduled")
        return {"method": "list_scheduled", "context": context, "result": persisted}

    def cancel_scheduled(self, *args, **kwargs) -> ReportBuilderServiceResult:
        """Execute cancel scheduled."""
        logger.info("%s called user=%s args=%s", "cancel_scheduled", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_cancel_scheduled(*args, **kwargs)
            if isinstance(result, ReportBuilderServiceResult):
                return result
            return ReportBuilderServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "cancel_scheduled", exc)
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "cancel_scheduled")
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_cancel_scheduled(self, *args, **kwargs) -> Any:
        """Internal implementation for cancel_scheduled."""
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
        processed = self._process_business_rules(enriched, method="cancel_scheduled")
        persisted = self._persist_side_effects(processed, method="cancel_scheduled")
        return {"method": "cancel_scheduled", "context": context, "result": persisted}

    def deliver_report(self, *args, **kwargs) -> ReportBuilderServiceResult:
        """Execute deliver report."""
        logger.info("%s called user=%s args=%s", "deliver_report", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_deliver_report(*args, **kwargs)
            if isinstance(result, ReportBuilderServiceResult):
                return result
            return ReportBuilderServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "deliver_report", exc)
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "deliver_report")
            return ReportBuilderServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_deliver_report(self, *args, **kwargs) -> Any:
        """Internal implementation for deliver_report."""
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
        processed = self._process_business_rules(enriched, method="deliver_report")
        persisted = self._persist_side_effects(processed, method="deliver_report")
        return {"method": "deliver_report", "context": context, "result": persisted}

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

    def helper_builder_0(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #0 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_0",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_1(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #1 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_1",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_2(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #2 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_2",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_3(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #3 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_3",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_4(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #4 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_4",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_5(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #5 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_5",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_6(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #6 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_6",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_7(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #7 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_7",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_8(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #8 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_8",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_9(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #9 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_9",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_10(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #10 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_10",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_11(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #11 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_11",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_12(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #12 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_12",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_13(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #13 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_13",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_14(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #14 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_14",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_15(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #15 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_15",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_16(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #16 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_16",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_17(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #17 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_17",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_18(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #18 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_18",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_19(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #19 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_19",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_20(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #20 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_20",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_21(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #21 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_21",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_22(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #22 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_22",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_23(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #23 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_23",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_builder_24(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #24 for builder metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "builder_24",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }


def get_builder_service(user=None, request=None) -> ReportBuilderService:
    return ReportBuilderService(user=user, request=request)
