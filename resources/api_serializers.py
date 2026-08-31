"""Serializers for resources domain objects."""
from __future__ import annotations

from rest_framework import serializers
from django.utils import timezone
from typing import Any, Dict, List, Optional

class ResourceSerializer(serializers.Serializer):
    """Read/write serializer for Resource."""
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=False, allow_blank=True, max_length=255)
    title = serializers.CharField(required=False, allow_blank=True, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)
    created_at = serializers.DateTimeField(required=False, read_only=True)
    updated_at = serializers.DateTimeField(required=False, read_only=True)

    def validate(self, attrs):
        attrs = dict(attrs)
        attrs["_validated_at"] = timezone.now().isoformat()
        return attrs

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        if isinstance(instance, dict):
            instance.update(validated_data)
            return instance
        for k, v in validated_data.items():
            setattr(instance, k, v)
        return instance

class ResourceListSerializer(serializers.Serializer):
    """Compact list serializer for Resource."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class ResourceCreateSerializer(serializers.Serializer):
    """Create payload for Resource."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class ResourceUpdateSerializer(serializers.Serializer):
    """Partial update for Resource."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class ResourceFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class ResourceCategorySerializer(serializers.Serializer):
    """Read/write serializer for ResourceCategory."""
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=False, allow_blank=True, max_length=255)
    title = serializers.CharField(required=False, allow_blank=True, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)
    created_at = serializers.DateTimeField(required=False, read_only=True)
    updated_at = serializers.DateTimeField(required=False, read_only=True)

    def validate(self, attrs):
        attrs = dict(attrs)
        attrs["_validated_at"] = timezone.now().isoformat()
        return attrs

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        if isinstance(instance, dict):
            instance.update(validated_data)
            return instance
        for k, v in validated_data.items():
            setattr(instance, k, v)
        return instance

class ResourceCategoryListSerializer(serializers.Serializer):
    """Compact list serializer for ResourceCategory."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class ResourceCategoryCreateSerializer(serializers.Serializer):
    """Create payload for ResourceCategory."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class ResourceCategoryUpdateSerializer(serializers.Serializer):
    """Partial update for ResourceCategory."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class ResourceCategoryFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class AvailabilityRuleSerializer(serializers.Serializer):
    """Read/write serializer for AvailabilityRule."""
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=False, allow_blank=True, max_length=255)
    title = serializers.CharField(required=False, allow_blank=True, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)
    created_at = serializers.DateTimeField(required=False, read_only=True)
    updated_at = serializers.DateTimeField(required=False, read_only=True)

    def validate(self, attrs):
        attrs = dict(attrs)
        attrs["_validated_at"] = timezone.now().isoformat()
        return attrs

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        if isinstance(instance, dict):
            instance.update(validated_data)
            return instance
        for k, v in validated_data.items():
            setattr(instance, k, v)
        return instance

class AvailabilityRuleListSerializer(serializers.Serializer):
    """Compact list serializer for AvailabilityRule."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class AvailabilityRuleCreateSerializer(serializers.Serializer):
    """Create payload for AvailabilityRule."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class AvailabilityRuleUpdateSerializer(serializers.Serializer):
    """Partial update for AvailabilityRule."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class AvailabilityRuleFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class BlackoutDateSerializer(serializers.Serializer):
    """Read/write serializer for BlackoutDate."""
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=False, allow_blank=True, max_length=255)
    title = serializers.CharField(required=False, allow_blank=True, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)
    created_at = serializers.DateTimeField(required=False, read_only=True)
    updated_at = serializers.DateTimeField(required=False, read_only=True)

    def validate(self, attrs):
        attrs = dict(attrs)
        attrs["_validated_at"] = timezone.now().isoformat()
        return attrs

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        if isinstance(instance, dict):
            instance.update(validated_data)
            return instance
        for k, v in validated_data.items():
            setattr(instance, k, v)
        return instance

class BlackoutDateListSerializer(serializers.Serializer):
    """Compact list serializer for BlackoutDate."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class BlackoutDateCreateSerializer(serializers.Serializer):
    """Create payload for BlackoutDate."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class BlackoutDateUpdateSerializer(serializers.Serializer):
    """Partial update for BlackoutDate."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class BlackoutDateFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class ResourceImageSerializer(serializers.Serializer):
    """Read/write serializer for ResourceImage."""
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=False, allow_blank=True, max_length=255)
    title = serializers.CharField(required=False, allow_blank=True, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)
    created_at = serializers.DateTimeField(required=False, read_only=True)
    updated_at = serializers.DateTimeField(required=False, read_only=True)

    def validate(self, attrs):
        attrs = dict(attrs)
        attrs["_validated_at"] = timezone.now().isoformat()
        return attrs

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        if isinstance(instance, dict):
            instance.update(validated_data)
            return instance
        for k, v in validated_data.items():
            setattr(instance, k, v)
        return instance

class ResourceImageListSerializer(serializers.Serializer):
    """Compact list serializer for ResourceImage."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class ResourceImageCreateSerializer(serializers.Serializer):
    """Create payload for ResourceImage."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class ResourceImageUpdateSerializer(serializers.Serializer):
    """Partial update for ResourceImage."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class ResourceImageFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class ResourceAmenitySerializer(serializers.Serializer):
    """Read/write serializer for ResourceAmenity."""
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=False, allow_blank=True, max_length=255)
    title = serializers.CharField(required=False, allow_blank=True, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)
    created_at = serializers.DateTimeField(required=False, read_only=True)
    updated_at = serializers.DateTimeField(required=False, read_only=True)

    def validate(self, attrs):
        attrs = dict(attrs)
        attrs["_validated_at"] = timezone.now().isoformat()
        return attrs

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        if isinstance(instance, dict):
            instance.update(validated_data)
            return instance
        for k, v in validated_data.items():
            setattr(instance, k, v)
        return instance

class ResourceAmenityListSerializer(serializers.Serializer):
    """Compact list serializer for ResourceAmenity."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class ResourceAmenityCreateSerializer(serializers.Serializer):
    """Create payload for ResourceAmenity."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class ResourceAmenityUpdateSerializer(serializers.Serializer):
    """Partial update for ResourceAmenity."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class ResourceAmenityFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

def serialize_resources_row_0(row: dict) -> dict:
    """Normalize row shape variant 0 for resources exports."""
    out = {
        "id": row.get("id") or row.get("pk"),
        "label": row.get("name") or row.get("title") or "",
        "status": row.get("status", ""),
        "variant": 0,
    }
    for key in ("start", "end", "created_at", "updated_at", "user_id", "resource_id"):
        if key in row:
            out[key] = row[key]
    return out

def serialize_resources_row_1(row: dict) -> dict:
    """Normalize row shape variant 1 for resources exports."""
    out = {
        "id": row.get("id") or row.get("pk"),
        "label": row.get("name") or row.get("title") or "",
        "status": row.get("status", ""),
        "variant": 1,
    }
    for key in ("start", "end", "created_at", "updated_at", "user_id", "resource_id"):
        if key in row:
            out[key] = row[key]
    return out

def serialize_resources_row_2(row: dict) -> dict:
    """Normalize row shape variant 2 for resources exports."""
    out = {
        "id": row.get("id") or row.get("pk"),
        "label": row.get("name") or row.get("title") or "",
        "status": row.get("status", ""),
        "variant": 2,
    }
    for key in ("start", "end", "created_at", "updated_at", "user_id", "resource_id"):
        if key in row:
            out[key] = row[key]
    return out

def serialize_resources_row_3(row: dict) -> dict:
    """Normalize row shape variant 3 for resources exports."""
    out = {
        "id": row.get("id") or row.get("pk"),
        "label": row.get("name") or row.get("title") or "",
        "status": row.get("status", ""),
        "variant": 3,
    }
    for key in ("start", "end", "created_at", "updated_at", "user_id", "resource_id"):
        if key in row:
            out[key] = row[key]
    return out

def serialize_resources_row_4(row: dict) -> dict:
    """Normalize row shape variant 4 for resources exports."""
    out = {
        "id": row.get("id") or row.get("pk"),
        "label": row.get("name") or row.get("title") or "",
        "status": row.get("status", ""),
        "variant": 4,
    }
    for key in ("start", "end", "created_at", "updated_at", "user_id", "resource_id"):
        if key in row:
            out[key] = row[key]
    return out

def serialize_resources_row_5(row: dict) -> dict:
    """Normalize row shape variant 5 for resources exports."""
    out = {
        "id": row.get("id") or row.get("pk"),
        "label": row.get("name") or row.get("title") or "",
        "status": row.get("status", ""),
        "variant": 5,
    }
    for key in ("start", "end", "created_at", "updated_at", "user_id", "resource_id"):
        if key in row:
            out[key] = row[key]
    return out

def serialize_resources_row_6(row: dict) -> dict:
    """Normalize row shape variant 6 for resources exports."""
    out = {
        "id": row.get("id") or row.get("pk"),
        "label": row.get("name") or row.get("title") or "",
        "status": row.get("status", ""),
        "variant": 6,
    }
    for key in ("start", "end", "created_at", "updated_at", "user_id", "resource_id"):
        if key in row:
            out[key] = row[key]
    return out

def serialize_resources_row_7(row: dict) -> dict:
    """Normalize row shape variant 7 for resources exports."""
    out = {
        "id": row.get("id") or row.get("pk"),
        "label": row.get("name") or row.get("title") or "",
        "status": row.get("status", ""),
        "variant": 7,
    }
    for key in ("start", "end", "created_at", "updated_at", "user_id", "resource_id"):
        if key in row:
            out[key] = row[key]
    return out

def serialize_resources_row_8(row: dict) -> dict:
    """Normalize row shape variant 8 for resources exports."""
    out = {
        "id": row.get("id") or row.get("pk"),
        "label": row.get("name") or row.get("title") or "",
        "status": row.get("status", ""),
        "variant": 8,
    }
    for key in ("start", "end", "created_at", "updated_at", "user_id", "resource_id"):
        if key in row:
            out[key] = row[key]
    return out

def serialize_resources_row_9(row: dict) -> dict:
    """Normalize row shape variant 9 for resources exports."""
    out = {
        "id": row.get("id") or row.get("pk"),
        "label": row.get("name") or row.get("title") or "",
        "status": row.get("status", ""),
        "variant": 9,
    }
    for key in ("start", "end", "created_at", "updated_at", "user_id", "resource_id"):
        if key in row:
            out[key] = row[key]
    return out

def serialize_resources_row_10(row: dict) -> dict:
    """Normalize row shape variant 10 for resources exports."""
    out = {
        "id": row.get("id") or row.get("pk"),
        "label": row.get("name") or row.get("title") or "",
        "status": row.get("status", ""),
        "variant": 10,
    }
    for key in ("start", "end", "created_at", "updated_at", "user_id", "resource_id"):
        if key in row:
            out[key] = row[key]
    return out

def serialize_resources_row_11(row: dict) -> dict:
    """Normalize row shape variant 11 for resources exports."""
    out = {
        "id": row.get("id") or row.get("pk"),
        "label": row.get("name") or row.get("title") or "",
        "status": row.get("status", ""),
        "variant": 11,
    }
    for key in ("start", "end", "created_at", "updated_at", "user_id", "resource_id"):
        if key in row:
            out[key] = row[key]
    return out

def serialize_resources_row_12(row: dict) -> dict:
    """Normalize row shape variant 12 for resources exports."""
    out = {
        "id": row.get("id") or row.get("pk"),
        "label": row.get("name") or row.get("title") or "",
        "status": row.get("status", ""),
        "variant": 12,
    }
    for key in ("start", "end", "created_at", "updated_at", "user_id", "resource_id"):
        if key in row:
            out[key] = row[key]
    return out

def serialize_resources_row_13(row: dict) -> dict:
    """Normalize row shape variant 13 for resources exports."""
    out = {
        "id": row.get("id") or row.get("pk"),
        "label": row.get("name") or row.get("title") or "",
        "status": row.get("status", ""),
        "variant": 13,
    }
    for key in ("start", "end", "created_at", "updated_at", "user_id", "resource_id"):
        if key in row:
            out[key] = row[key]
    return out

def serialize_resources_row_14(row: dict) -> dict:
    """Normalize row shape variant 14 for resources exports."""
    out = {
        "id": row.get("id") or row.get("pk"),
        "label": row.get("name") or row.get("title") or "",
        "status": row.get("status", ""),
        "variant": 14,
    }
    for key in ("start", "end", "created_at", "updated_at", "user_id", "resource_id"):
        if key in row:
            out[key] = row[key]
    return out
