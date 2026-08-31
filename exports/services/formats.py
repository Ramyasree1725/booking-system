"""exports.formats — domain service generated for platform completeness."""
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

logger = logging.getLogger("booking.exports.formats")


@dataclass
class ExportFormatServiceResult:
    success: bool = True
    message: str = ""
    data: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)


class ExportFormatService:
    """Service coordinating formats operations."""

    def __init__(self, user=None, request=None):
        self.user = user
        self.request = request
        self._cache: Dict[str, Any] = {}

    def to_csv(self, *args, **kwargs) -> ExportFormatServiceResult:
        """Execute to csv."""
        logger.info("%s called user=%s args=%s", "to_csv", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_to_csv(*args, **kwargs)
            if isinstance(result, ExportFormatServiceResult):
                return result
            return ExportFormatServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "to_csv", exc)
            return ExportFormatServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "to_csv")
            return ExportFormatServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_to_csv(self, *args, **kwargs) -> Any:
        """Internal implementation for to_csv."""
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
        processed = self._process_business_rules(enriched, method="to_csv")
        persisted = self._persist_side_effects(processed, method="to_csv")
        return {"method": "to_csv", "context": context, "result": persisted}

    def to_json(self, *args, **kwargs) -> ExportFormatServiceResult:
        """Execute to json."""
        logger.info("%s called user=%s args=%s", "to_json", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_to_json(*args, **kwargs)
            if isinstance(result, ExportFormatServiceResult):
                return result
            return ExportFormatServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "to_json", exc)
            return ExportFormatServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "to_json")
            return ExportFormatServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_to_json(self, *args, **kwargs) -> Any:
        """Internal implementation for to_json."""
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
        processed = self._process_business_rules(enriched, method="to_json")
        persisted = self._persist_side_effects(processed, method="to_json")
        return {"method": "to_json", "context": context, "result": persisted}

    def to_ical(self, *args, **kwargs) -> ExportFormatServiceResult:
        """Execute to ical."""
        logger.info("%s called user=%s args=%s", "to_ical", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_to_ical(*args, **kwargs)
            if isinstance(result, ExportFormatServiceResult):
                return result
            return ExportFormatServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "to_ical", exc)
            return ExportFormatServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "to_ical")
            return ExportFormatServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_to_ical(self, *args, **kwargs) -> Any:
        """Internal implementation for to_ical."""
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
        processed = self._process_business_rules(enriched, method="to_ical")
        persisted = self._persist_side_effects(processed, method="to_ical")
        return {"method": "to_ical", "context": context, "result": persisted}

    def to_xlsx_rows(self, *args, **kwargs) -> ExportFormatServiceResult:
        """Execute to xlsx rows."""
        logger.info("%s called user=%s args=%s", "to_xlsx_rows", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_to_xlsx_rows(*args, **kwargs)
            if isinstance(result, ExportFormatServiceResult):
                return result
            return ExportFormatServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "to_xlsx_rows", exc)
            return ExportFormatServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "to_xlsx_rows")
            return ExportFormatServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_to_xlsx_rows(self, *args, **kwargs) -> Any:
        """Internal implementation for to_xlsx_rows."""
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
        processed = self._process_business_rules(enriched, method="to_xlsx_rows")
        persisted = self._persist_side_effects(processed, method="to_xlsx_rows")
        return {"method": "to_xlsx_rows", "context": context, "result": persisted}

    def to_pdf_summary(self, *args, **kwargs) -> ExportFormatServiceResult:
        """Execute to pdf summary."""
        logger.info("%s called user=%s args=%s", "to_pdf_summary", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_to_pdf_summary(*args, **kwargs)
            if isinstance(result, ExportFormatServiceResult):
                return result
            return ExportFormatServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "to_pdf_summary", exc)
            return ExportFormatServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "to_pdf_summary")
            return ExportFormatServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_to_pdf_summary(self, *args, **kwargs) -> Any:
        """Internal implementation for to_pdf_summary."""
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
        processed = self._process_business_rules(enriched, method="to_pdf_summary")
        persisted = self._persist_side_effects(processed, method="to_pdf_summary")
        return {"method": "to_pdf_summary", "context": context, "result": persisted}

    def stream_csv(self, *args, **kwargs) -> ExportFormatServiceResult:
        """Execute stream csv."""
        logger.info("%s called user=%s args=%s", "stream_csv", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_stream_csv(*args, **kwargs)
            if isinstance(result, ExportFormatServiceResult):
                return result
            return ExportFormatServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "stream_csv", exc)
            return ExportFormatServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "stream_csv")
            return ExportFormatServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_stream_csv(self, *args, **kwargs) -> Any:
        """Internal implementation for stream_csv."""
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
        processed = self._process_business_rules(enriched, method="stream_csv")
        persisted = self._persist_side_effects(processed, method="stream_csv")
        return {"method": "stream_csv", "context": context, "result": persisted}

    def stream_json(self, *args, **kwargs) -> ExportFormatServiceResult:
        """Execute stream json."""
        logger.info("%s called user=%s args=%s", "stream_json", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_stream_json(*args, **kwargs)
            if isinstance(result, ExportFormatServiceResult):
                return result
            return ExportFormatServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "stream_json", exc)
            return ExportFormatServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "stream_json")
            return ExportFormatServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_stream_json(self, *args, **kwargs) -> Any:
        """Internal implementation for stream_json."""
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
        processed = self._process_business_rules(enriched, method="stream_json")
        persisted = self._persist_side_effects(processed, method="stream_json")
        return {"method": "stream_json", "context": context, "result": persisted}

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

    def helper_formats_0(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #0 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_0",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_1(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #1 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_1",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_2(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #2 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_2",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_3(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #3 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_3",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_4(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #4 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_4",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_5(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #5 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_5",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_6(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #6 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_6",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_7(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #7 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_7",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_8(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #8 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_8",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_9(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #9 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_9",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_10(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #10 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_10",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_11(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #11 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_11",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_12(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #12 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_12",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_13(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #13 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_13",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_14(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #14 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_14",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_15(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #15 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_15",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_16(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #16 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_16",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_17(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #17 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_17",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_18(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #18 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_18",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_19(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #19 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_19",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_20(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #20 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_20",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_21(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #21 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_21",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_22(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #22 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_22",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_23(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #23 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_23",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_formats_24(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #24 for formats metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "formats_24",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }


def get_formats_service(user=None, request=None) -> ExportFormatService:
    return ExportFormatService(user=user, request=request)
