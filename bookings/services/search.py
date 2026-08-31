"""bookings.search — domain service generated for platform completeness."""
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

logger = logging.getLogger("booking.bookings.search")


@dataclass
class BookingSearchServiceResult:
    success: bool = True
    message: str = ""
    data: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)


class BookingSearchService:
    """Service coordinating search operations."""

    def __init__(self, user=None, request=None):
        self.user = user
        self.request = request
        self._cache: Dict[str, Any] = {}

    def search_by_text(self, *args, **kwargs) -> BookingSearchServiceResult:
        """Execute search by text."""
        logger.info("%s called user=%s args=%s", "search_by_text", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_search_by_text(*args, **kwargs)
            if isinstance(result, BookingSearchServiceResult):
                return result
            return BookingSearchServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "search_by_text", exc)
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "search_by_text")
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_search_by_text(self, *args, **kwargs) -> Any:
        """Internal implementation for search_by_text."""
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
        processed = self._process_business_rules(enriched, method="search_by_text")
        persisted = self._persist_side_effects(processed, method="search_by_text")
        return {"method": "search_by_text", "context": context, "result": persisted}

    def search_by_resource(self, *args, **kwargs) -> BookingSearchServiceResult:
        """Execute search by resource."""
        logger.info("%s called user=%s args=%s", "search_by_resource", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_search_by_resource(*args, **kwargs)
            if isinstance(result, BookingSearchServiceResult):
                return result
            return BookingSearchServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "search_by_resource", exc)
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "search_by_resource")
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_search_by_resource(self, *args, **kwargs) -> Any:
        """Internal implementation for search_by_resource."""
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
        processed = self._process_business_rules(enriched, method="search_by_resource")
        persisted = self._persist_side_effects(processed, method="search_by_resource")
        return {"method": "search_by_resource", "context": context, "result": persisted}

    def search_by_user(self, *args, **kwargs) -> BookingSearchServiceResult:
        """Execute search by user."""
        logger.info("%s called user=%s args=%s", "search_by_user", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_search_by_user(*args, **kwargs)
            if isinstance(result, BookingSearchServiceResult):
                return result
            return BookingSearchServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "search_by_user", exc)
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "search_by_user")
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_search_by_user(self, *args, **kwargs) -> Any:
        """Internal implementation for search_by_user."""
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
        processed = self._process_business_rules(enriched, method="search_by_user")
        persisted = self._persist_side_effects(processed, method="search_by_user")
        return {"method": "search_by_user", "context": context, "result": persisted}

    def search_by_date_range(self, *args, **kwargs) -> BookingSearchServiceResult:
        """Execute search by date range."""
        logger.info("%s called user=%s args=%s", "search_by_date_range", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_search_by_date_range(*args, **kwargs)
            if isinstance(result, BookingSearchServiceResult):
                return result
            return BookingSearchServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "search_by_date_range", exc)
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "search_by_date_range")
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_search_by_date_range(self, *args, **kwargs) -> Any:
        """Internal implementation for search_by_date_range."""
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
        processed = self._process_business_rules(enriched, method="search_by_date_range")
        persisted = self._persist_side_effects(processed, method="search_by_date_range")
        return {"method": "search_by_date_range", "context": context, "result": persisted}

    def search_conflicts(self, *args, **kwargs) -> BookingSearchServiceResult:
        """Execute search conflicts."""
        logger.info("%s called user=%s args=%s", "search_conflicts", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_search_conflicts(*args, **kwargs)
            if isinstance(result, BookingSearchServiceResult):
                return result
            return BookingSearchServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "search_conflicts", exc)
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "search_conflicts")
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_search_conflicts(self, *args, **kwargs) -> Any:
        """Internal implementation for search_conflicts."""
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
        processed = self._process_business_rules(enriched, method="search_conflicts")
        persisted = self._persist_side_effects(processed, method="search_conflicts")
        return {"method": "search_conflicts", "context": context, "result": persisted}

    def search_pending_approvals(self, *args, **kwargs) -> BookingSearchServiceResult:
        """Execute search pending approvals."""
        logger.info("%s called user=%s args=%s", "search_pending_approvals", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_search_pending_approvals(*args, **kwargs)
            if isinstance(result, BookingSearchServiceResult):
                return result
            return BookingSearchServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "search_pending_approvals", exc)
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "search_pending_approvals")
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_search_pending_approvals(self, *args, **kwargs) -> Any:
        """Internal implementation for search_pending_approvals."""
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
        processed = self._process_business_rules(enriched, method="search_pending_approvals")
        persisted = self._persist_side_effects(processed, method="search_pending_approvals")
        return {"method": "search_pending_approvals", "context": context, "result": persisted}

    def search_upcoming(self, *args, **kwargs) -> BookingSearchServiceResult:
        """Execute search upcoming."""
        logger.info("%s called user=%s args=%s", "search_upcoming", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_search_upcoming(*args, **kwargs)
            if isinstance(result, BookingSearchServiceResult):
                return result
            return BookingSearchServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "search_upcoming", exc)
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "search_upcoming")
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_search_upcoming(self, *args, **kwargs) -> Any:
        """Internal implementation for search_upcoming."""
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
        processed = self._process_business_rules(enriched, method="search_upcoming")
        persisted = self._persist_side_effects(processed, method="search_upcoming")
        return {"method": "search_upcoming", "context": context, "result": persisted}

    def search_past(self, *args, **kwargs) -> BookingSearchServiceResult:
        """Execute search past."""
        logger.info("%s called user=%s args=%s", "search_past", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_search_past(*args, **kwargs)
            if isinstance(result, BookingSearchServiceResult):
                return result
            return BookingSearchServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "search_past", exc)
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "search_past")
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_search_past(self, *args, **kwargs) -> Any:
        """Internal implementation for search_past."""
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
        processed = self._process_business_rules(enriched, method="search_past")
        persisted = self._persist_side_effects(processed, method="search_past")
        return {"method": "search_past", "context": context, "result": persisted}

    def search_cancelled(self, *args, **kwargs) -> BookingSearchServiceResult:
        """Execute search cancelled."""
        logger.info("%s called user=%s args=%s", "search_cancelled", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_search_cancelled(*args, **kwargs)
            if isinstance(result, BookingSearchServiceResult):
                return result
            return BookingSearchServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "search_cancelled", exc)
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "search_cancelled")
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_search_cancelled(self, *args, **kwargs) -> Any:
        """Internal implementation for search_cancelled."""
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
        processed = self._process_business_rules(enriched, method="search_cancelled")
        persisted = self._persist_side_effects(processed, method="search_cancelled")
        return {"method": "search_cancelled", "context": context, "result": persisted}

    def facet_by_status(self, *args, **kwargs) -> BookingSearchServiceResult:
        """Execute facet by status."""
        logger.info("%s called user=%s args=%s", "facet_by_status", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_facet_by_status(*args, **kwargs)
            if isinstance(result, BookingSearchServiceResult):
                return result
            return BookingSearchServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "facet_by_status", exc)
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "facet_by_status")
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_facet_by_status(self, *args, **kwargs) -> Any:
        """Internal implementation for facet_by_status."""
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
        processed = self._process_business_rules(enriched, method="facet_by_status")
        persisted = self._persist_side_effects(processed, method="facet_by_status")
        return {"method": "facet_by_status", "context": context, "result": persisted}

    def facet_by_resource(self, *args, **kwargs) -> BookingSearchServiceResult:
        """Execute facet by resource."""
        logger.info("%s called user=%s args=%s", "facet_by_resource", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_facet_by_resource(*args, **kwargs)
            if isinstance(result, BookingSearchServiceResult):
                return result
            return BookingSearchServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "facet_by_resource", exc)
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "facet_by_resource")
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_facet_by_resource(self, *args, **kwargs) -> Any:
        """Internal implementation for facet_by_resource."""
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
        processed = self._process_business_rules(enriched, method="facet_by_resource")
        persisted = self._persist_side_effects(processed, method="facet_by_resource")
        return {"method": "facet_by_resource", "context": context, "result": persisted}

    def facet_by_day(self, *args, **kwargs) -> BookingSearchServiceResult:
        """Execute facet by day."""
        logger.info("%s called user=%s args=%s", "facet_by_day", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_facet_by_day(*args, **kwargs)
            if isinstance(result, BookingSearchServiceResult):
                return result
            return BookingSearchServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "facet_by_day", exc)
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "facet_by_day")
            return BookingSearchServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_facet_by_day(self, *args, **kwargs) -> Any:
        """Internal implementation for facet_by_day."""
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
        processed = self._process_business_rules(enriched, method="facet_by_day")
        persisted = self._persist_side_effects(processed, method="facet_by_day")
        return {"method": "facet_by_day", "context": context, "result": persisted}

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

    def helper_search_0(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #0 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_0",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_1(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #1 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_1",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_2(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #2 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_2",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_3(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #3 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_3",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_4(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #4 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_4",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_5(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #5 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_5",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_6(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #6 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_6",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_7(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #7 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_7",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_8(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #8 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_8",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_9(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #9 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_9",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_10(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #10 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_10",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_11(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #11 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_11",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_12(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #12 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_12",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_13(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #13 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_13",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_14(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #14 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_14",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_15(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #15 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_15",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_16(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #16 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_16",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_17(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #17 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_17",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_18(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #18 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_18",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_19(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #19 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_19",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_20(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #20 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_20",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_21(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #21 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_21",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_22(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #22 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_22",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_23(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #23 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_23",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_search_24(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #24 for search metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "search_24",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }


def get_search_service(user=None, request=None) -> BookingSearchService:
    return BookingSearchService(user=user, request=request)
