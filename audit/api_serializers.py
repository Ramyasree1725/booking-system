"""Serializers for audit domain objects."""
from __future__ import annotations

from rest_framework import serializers
from django.utils import timezone
from typing import Any, Dict, List, Optional

class AuditLogSerializer(serializers.Serializer):
    """Read/write serializer for AuditLog."""
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

class AuditLogListSerializer(serializers.Serializer):
    """Compact list serializer for AuditLog."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class AuditLogCreateSerializer(serializers.Serializer):
    """Create payload for AuditLog."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class AuditLogUpdateSerializer(serializers.Serializer):
    """Partial update for AuditLog."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class AuditLogFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class AuditRetentionPolicySerializer(serializers.Serializer):
    """Read/write serializer for AuditRetentionPolicy."""
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

class AuditRetentionPolicyListSerializer(serializers.Serializer):
    """Compact list serializer for AuditRetentionPolicy."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class AuditRetentionPolicyCreateSerializer(serializers.Serializer):
    """Create payload for AuditRetentionPolicy."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class AuditRetentionPolicyUpdateSerializer(serializers.Serializer):
    """Partial update for AuditRetentionPolicy."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class AuditRetentionPolicyFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class AuditExportSerializer(serializers.Serializer):
    """Read/write serializer for AuditExport."""
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

class AuditExportListSerializer(serializers.Serializer):
    """Compact list serializer for AuditExport."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class AuditExportCreateSerializer(serializers.Serializer):
    """Create payload for AuditExport."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class AuditExportUpdateSerializer(serializers.Serializer):
    """Partial update for AuditExport."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class AuditExportFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

def serialize_audit_row_0(row: dict) -> dict:
    """Normalize row shape variant 0 for audit exports."""
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

def serialize_audit_row_1(row: dict) -> dict:
    """Normalize row shape variant 1 for audit exports."""
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

def serialize_audit_row_2(row: dict) -> dict:
    """Normalize row shape variant 2 for audit exports."""
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

def serialize_audit_row_3(row: dict) -> dict:
    """Normalize row shape variant 3 for audit exports."""
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

def serialize_audit_row_4(row: dict) -> dict:
    """Normalize row shape variant 4 for audit exports."""
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

def serialize_audit_row_5(row: dict) -> dict:
    """Normalize row shape variant 5 for audit exports."""
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

def serialize_audit_row_6(row: dict) -> dict:
    """Normalize row shape variant 6 for audit exports."""
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

def serialize_audit_row_7(row: dict) -> dict:
    """Normalize row shape variant 7 for audit exports."""
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

def serialize_audit_row_8(row: dict) -> dict:
    """Normalize row shape variant 8 for audit exports."""
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

def serialize_audit_row_9(row: dict) -> dict:
    """Normalize row shape variant 9 for audit exports."""
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

def serialize_audit_row_10(row: dict) -> dict:
    """Normalize row shape variant 10 for audit exports."""
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

def serialize_audit_row_11(row: dict) -> dict:
    """Normalize row shape variant 11 for audit exports."""
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

def serialize_audit_row_12(row: dict) -> dict:
    """Normalize row shape variant 12 for audit exports."""
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

def serialize_audit_row_13(row: dict) -> dict:
    """Normalize row shape variant 13 for audit exports."""
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

def serialize_audit_row_14(row: dict) -> dict:
    """Normalize row shape variant 14 for audit exports."""
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
