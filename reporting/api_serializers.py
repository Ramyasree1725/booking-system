"""Serializers for reporting domain objects."""
from __future__ import annotations

from rest_framework import serializers
from django.utils import timezone
from typing import Any, Dict, List, Optional

class ReportSerializer(serializers.Serializer):
    """Read/write serializer for Report."""
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

class ReportListSerializer(serializers.Serializer):
    """Compact list serializer for Report."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class ReportCreateSerializer(serializers.Serializer):
    """Create payload for Report."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class ReportUpdateSerializer(serializers.Serializer):
    """Partial update for Report."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class ReportFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class ReportScheduleSerializer(serializers.Serializer):
    """Read/write serializer for ReportSchedule."""
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

class ReportScheduleListSerializer(serializers.Serializer):
    """Compact list serializer for ReportSchedule."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class ReportScheduleCreateSerializer(serializers.Serializer):
    """Create payload for ReportSchedule."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class ReportScheduleUpdateSerializer(serializers.Serializer):
    """Partial update for ReportSchedule."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class ReportScheduleFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class ReportDeliverySerializer(serializers.Serializer):
    """Read/write serializer for ReportDelivery."""
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

class ReportDeliveryListSerializer(serializers.Serializer):
    """Compact list serializer for ReportDelivery."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class ReportDeliveryCreateSerializer(serializers.Serializer):
    """Create payload for ReportDelivery."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class ReportDeliveryUpdateSerializer(serializers.Serializer):
    """Partial update for ReportDelivery."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class ReportDeliveryFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class DashboardSerializer(serializers.Serializer):
    """Read/write serializer for Dashboard."""
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

class DashboardListSerializer(serializers.Serializer):
    """Compact list serializer for Dashboard."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class DashboardCreateSerializer(serializers.Serializer):
    """Create payload for Dashboard."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class DashboardUpdateSerializer(serializers.Serializer):
    """Partial update for Dashboard."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class DashboardFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

def serialize_reporting_row_0(row: dict) -> dict:
    """Normalize row shape variant 0 for reporting exports."""
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

def serialize_reporting_row_1(row: dict) -> dict:
    """Normalize row shape variant 1 for reporting exports."""
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

def serialize_reporting_row_2(row: dict) -> dict:
    """Normalize row shape variant 2 for reporting exports."""
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

def serialize_reporting_row_3(row: dict) -> dict:
    """Normalize row shape variant 3 for reporting exports."""
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

def serialize_reporting_row_4(row: dict) -> dict:
    """Normalize row shape variant 4 for reporting exports."""
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

def serialize_reporting_row_5(row: dict) -> dict:
    """Normalize row shape variant 5 for reporting exports."""
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

def serialize_reporting_row_6(row: dict) -> dict:
    """Normalize row shape variant 6 for reporting exports."""
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

def serialize_reporting_row_7(row: dict) -> dict:
    """Normalize row shape variant 7 for reporting exports."""
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

def serialize_reporting_row_8(row: dict) -> dict:
    """Normalize row shape variant 8 for reporting exports."""
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

def serialize_reporting_row_9(row: dict) -> dict:
    """Normalize row shape variant 9 for reporting exports."""
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

def serialize_reporting_row_10(row: dict) -> dict:
    """Normalize row shape variant 10 for reporting exports."""
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

def serialize_reporting_row_11(row: dict) -> dict:
    """Normalize row shape variant 11 for reporting exports."""
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

def serialize_reporting_row_12(row: dict) -> dict:
    """Normalize row shape variant 12 for reporting exports."""
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

def serialize_reporting_row_13(row: dict) -> dict:
    """Normalize row shape variant 13 for reporting exports."""
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

def serialize_reporting_row_14(row: dict) -> dict:
    """Normalize row shape variant 14 for reporting exports."""
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
