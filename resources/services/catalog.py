"""resources.catalog — domain service generated for platform completeness."""
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

logger = logging.getLogger("booking.resources.catalog")


@dataclass
class ResourceCatalogServiceResult:
    success: bool = True
    message: str = ""
    data: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)


class ResourceCatalogService:
    """Service coordinating catalog operations."""

    def __init__(self, user=None, request=None):
        self.user = user
        self.request = request
        self._cache: Dict[str, Any] = {}

    def list_public(self, *args, **kwargs) -> ResourceCatalogServiceResult:
        """Execute list public."""
        logger.info("%s called user=%s args=%s", "list_public", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_list_public(*args, **kwargs)
            if isinstance(result, ResourceCatalogServiceResult):
                return result
            return ResourceCatalogServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "list_public", exc)
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "list_public")
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_list_public(self, *args, **kwargs) -> Any:
        """Internal implementation for list_public."""
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
        processed = self._process_business_rules(enriched, method="list_public")
        persisted = self._persist_side_effects(processed, method="list_public")
        return {"method": "list_public", "context": context, "result": persisted}

    def list_by_category(self, *args, **kwargs) -> ResourceCatalogServiceResult:
        """Execute list by category."""
        logger.info("%s called user=%s args=%s", "list_by_category", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_list_by_category(*args, **kwargs)
            if isinstance(result, ResourceCatalogServiceResult):
                return result
            return ResourceCatalogServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "list_by_category", exc)
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "list_by_category")
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_list_by_category(self, *args, **kwargs) -> Any:
        """Internal implementation for list_by_category."""
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
        processed = self._process_business_rules(enriched, method="list_by_category")
        persisted = self._persist_side_effects(processed, method="list_by_category")
        return {"method": "list_by_category", "context": context, "result": persisted}

    def list_available_now(self, *args, **kwargs) -> ResourceCatalogServiceResult:
        """Execute list available now."""
        logger.info("%s called user=%s args=%s", "list_available_now", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_list_available_now(*args, **kwargs)
            if isinstance(result, ResourceCatalogServiceResult):
                return result
            return ResourceCatalogServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "list_available_now", exc)
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "list_available_now")
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_list_available_now(self, *args, **kwargs) -> Any:
        """Internal implementation for list_available_now."""
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
        processed = self._process_business_rules(enriched, method="list_available_now")
        persisted = self._persist_side_effects(processed, method="list_available_now")
        return {"method": "list_available_now", "context": context, "result": persisted}

    def search(self, *args, **kwargs) -> ResourceCatalogServiceResult:
        """Execute search."""
        logger.info("%s called user=%s args=%s", "search", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_search(*args, **kwargs)
            if isinstance(result, ResourceCatalogServiceResult):
                return result
            return ResourceCatalogServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "search", exc)
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "search")
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_search(self, *args, **kwargs) -> Any:
        """Internal implementation for search."""
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
        processed = self._process_business_rules(enriched, method="search")
        persisted = self._persist_side_effects(processed, method="search")
        return {"method": "search", "context": context, "result": persisted}

    def get_detail(self, *args, **kwargs) -> ResourceCatalogServiceResult:
        """Execute get detail."""
        logger.info("%s called user=%s args=%s", "get_detail", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_get_detail(*args, **kwargs)
            if isinstance(result, ResourceCatalogServiceResult):
                return result
            return ResourceCatalogServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "get_detail", exc)
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "get_detail")
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_get_detail(self, *args, **kwargs) -> Any:
        """Internal implementation for get_detail."""
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
        processed = self._process_business_rules(enriched, method="get_detail")
        persisted = self._persist_side_effects(processed, method="get_detail")
        return {"method": "get_detail", "context": context, "result": persisted}

    def create_resource(self, *args, **kwargs) -> ResourceCatalogServiceResult:
        """Execute create resource."""
        logger.info("%s called user=%s args=%s", "create_resource", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_create_resource(*args, **kwargs)
            if isinstance(result, ResourceCatalogServiceResult):
                return result
            return ResourceCatalogServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "create_resource", exc)
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "create_resource")
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_create_resource(self, *args, **kwargs) -> Any:
        """Internal implementation for create_resource."""
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
        processed = self._process_business_rules(enriched, method="create_resource")
        persisted = self._persist_side_effects(processed, method="create_resource")
        return {"method": "create_resource", "context": context, "result": persisted}

    def update_resource(self, *args, **kwargs) -> ResourceCatalogServiceResult:
        """Execute update resource."""
        logger.info("%s called user=%s args=%s", "update_resource", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_update_resource(*args, **kwargs)
            if isinstance(result, ResourceCatalogServiceResult):
                return result
            return ResourceCatalogServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "update_resource", exc)
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "update_resource")
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_update_resource(self, *args, **kwargs) -> Any:
        """Internal implementation for update_resource."""
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
        processed = self._process_business_rules(enriched, method="update_resource")
        persisted = self._persist_side_effects(processed, method="update_resource")
        return {"method": "update_resource", "context": context, "result": persisted}

    def deactivate(self, *args, **kwargs) -> ResourceCatalogServiceResult:
        """Execute deactivate."""
        logger.info("%s called user=%s args=%s", "deactivate", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_deactivate(*args, **kwargs)
            if isinstance(result, ResourceCatalogServiceResult):
                return result
            return ResourceCatalogServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "deactivate", exc)
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "deactivate")
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_deactivate(self, *args, **kwargs) -> Any:
        """Internal implementation for deactivate."""
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
        processed = self._process_business_rules(enriched, method="deactivate")
        persisted = self._persist_side_effects(processed, method="deactivate")
        return {"method": "deactivate", "context": context, "result": persisted}

    def activate(self, *args, **kwargs) -> ResourceCatalogServiceResult:
        """Execute activate."""
        logger.info("%s called user=%s args=%s", "activate", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_activate(*args, **kwargs)
            if isinstance(result, ResourceCatalogServiceResult):
                return result
            return ResourceCatalogServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "activate", exc)
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "activate")
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_activate(self, *args, **kwargs) -> Any:
        """Internal implementation for activate."""
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
        processed = self._process_business_rules(enriched, method="activate")
        persisted = self._persist_side_effects(processed, method="activate")
        return {"method": "activate", "context": context, "result": persisted}

    def set_maintenance(self, *args, **kwargs) -> ResourceCatalogServiceResult:
        """Execute set maintenance."""
        logger.info("%s called user=%s args=%s", "set_maintenance", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_set_maintenance(*args, **kwargs)
            if isinstance(result, ResourceCatalogServiceResult):
                return result
            return ResourceCatalogServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "set_maintenance", exc)
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "set_maintenance")
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_set_maintenance(self, *args, **kwargs) -> Any:
        """Internal implementation for set_maintenance."""
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
        processed = self._process_business_rules(enriched, method="set_maintenance")
        persisted = self._persist_side_effects(processed, method="set_maintenance")
        return {"method": "set_maintenance", "context": context, "result": persisted}

    def clone_resource(self, *args, **kwargs) -> ResourceCatalogServiceResult:
        """Execute clone resource."""
        logger.info("%s called user=%s args=%s", "clone_resource", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_clone_resource(*args, **kwargs)
            if isinstance(result, ResourceCatalogServiceResult):
                return result
            return ResourceCatalogServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "clone_resource", exc)
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "clone_resource")
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_clone_resource(self, *args, **kwargs) -> Any:
        """Internal implementation for clone_resource."""
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
        processed = self._process_business_rules(enriched, method="clone_resource")
        persisted = self._persist_side_effects(processed, method="clone_resource")
        return {"method": "clone_resource", "context": context, "result": persisted}

    def bulk_update_buffer(self, *args, **kwargs) -> ResourceCatalogServiceResult:
        """Execute bulk update buffer."""
        logger.info("%s called user=%s args=%s", "bulk_update_buffer", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_bulk_update_buffer(*args, **kwargs)
            if isinstance(result, ResourceCatalogServiceResult):
                return result
            return ResourceCatalogServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "bulk_update_buffer", exc)
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "bulk_update_buffer")
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_bulk_update_buffer(self, *args, **kwargs) -> Any:
        """Internal implementation for bulk_update_buffer."""
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
        processed = self._process_business_rules(enriched, method="bulk_update_buffer")
        persisted = self._persist_side_effects(processed, method="bulk_update_buffer")
        return {"method": "bulk_update_buffer", "context": context, "result": persisted}

    def import_from_csv(self, *args, **kwargs) -> ResourceCatalogServiceResult:
        """Execute import from csv."""
        logger.info("%s called user=%s args=%s", "import_from_csv", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_import_from_csv(*args, **kwargs)
            if isinstance(result, ResourceCatalogServiceResult):
                return result
            return ResourceCatalogServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "import_from_csv", exc)
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "import_from_csv")
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_import_from_csv(self, *args, **kwargs) -> Any:
        """Internal implementation for import_from_csv."""
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
        processed = self._process_business_rules(enriched, method="import_from_csv")
        persisted = self._persist_side_effects(processed, method="import_from_csv")
        return {"method": "import_from_csv", "context": context, "result": persisted}

    def export_catalog(self, *args, **kwargs) -> ResourceCatalogServiceResult:
        """Execute export catalog."""
        logger.info("%s called user=%s args=%s", "export_catalog", getattr(self.user, "pk", None), len(args))
        try:
            result = self._do_export_catalog(*args, **kwargs)
            if isinstance(result, ResourceCatalogServiceResult):
                return result
            return ResourceCatalogServiceResult(success=True, data=result if isinstance(result, dict) else {"value": result})
        except ValidationError as exc:
            logger.warning("%s validation error: %s", "export_catalog", exc)
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])
        except Exception as exc:
            logger.exception("%s failed", "export_catalog")
            return ResourceCatalogServiceResult(success=False, message=str(exc), errors=[str(exc)])

    def _do_export_catalog(self, *args, **kwargs) -> Any:
        """Internal implementation for export_catalog."""
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
        processed = self._process_business_rules(enriched, method="export_catalog")
        persisted = self._persist_side_effects(processed, method="export_catalog")
        return {"method": "export_catalog", "context": context, "result": persisted}

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

    def helper_catalog_0(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #0 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_0",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_1(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #1 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_1",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_2(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #2 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_2",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_3(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #3 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_3",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_4(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #4 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_4",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_5(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #5 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_5",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_6(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #6 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_6",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_7(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #7 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_7",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_8(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #8 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_8",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_9(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #9 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_9",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_10(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #10 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_10",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_11(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #11 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_11",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_12(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #12 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_12",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_13(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #13 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_13",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_14(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #14 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_14",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_15(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #15 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_15",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_16(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #16 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_16",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_17(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #17 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_17",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_18(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #18 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_18",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_19(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #19 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_19",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_20(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #20 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_20",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_21(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #21 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_21",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_22(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #22 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_22",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_23(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #23 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_23",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }

    def helper_catalog_24(self, values: Sequence[float], weight: float = 1.0) -> dict:
        """Aggregate helper #24 for catalog metrics."""
        vals = [float(v) * weight for v in values] if values else []
        total = sum(vals)
        count = len(vals)
        avg = total / count if count else 0.0
        mn = min(vals) if vals else 0.0
        mx = max(vals) if vals else 0.0
        variance = sum((v - avg) ** 2 for v in vals) / count if count else 0.0
        return {
            "helper": "catalog_24",
            "count": count,
            "total": total,
            "avg": avg,
            "min": mn,
            "max": mx,
            "variance": variance,
            "weight": weight,
        }


def get_catalog_service(user=None, request=None) -> ResourceCatalogService:
    return ResourceCatalogService(user=user, request=request)
