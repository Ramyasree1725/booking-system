"""Serializers for notifications domain objects."""
from __future__ import annotations

from rest_framework import serializers
from django.utils import timezone
from typing import Any, Dict, List, Optional

class NotificationSerializer(serializers.Serializer):
    """Read/write serializer for Notification."""
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

class NotificationListSerializer(serializers.Serializer):
    """Compact list serializer for Notification."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class NotificationCreateSerializer(serializers.Serializer):
    """Create payload for Notification."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class NotificationUpdateSerializer(serializers.Serializer):
    """Partial update for Notification."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class NotificationFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class NotificationTemplateSerializer(serializers.Serializer):
    """Read/write serializer for NotificationTemplate."""
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

class NotificationTemplateListSerializer(serializers.Serializer):
    """Compact list serializer for NotificationTemplate."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class NotificationTemplateCreateSerializer(serializers.Serializer):
    """Create payload for NotificationTemplate."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class NotificationTemplateUpdateSerializer(serializers.Serializer):
    """Partial update for NotificationTemplate."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class NotificationTemplateFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class NotificationDeliverySerializer(serializers.Serializer):
    """Read/write serializer for NotificationDelivery."""
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

class NotificationDeliveryListSerializer(serializers.Serializer):
    """Compact list serializer for NotificationDelivery."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class NotificationDeliveryCreateSerializer(serializers.Serializer):
    """Create payload for NotificationDelivery."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class NotificationDeliveryUpdateSerializer(serializers.Serializer):
    """Partial update for NotificationDelivery."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class NotificationDeliveryFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class DigestSerializer(serializers.Serializer):
    """Read/write serializer for Digest."""
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

class DigestListSerializer(serializers.Serializer):
    """Compact list serializer for Digest."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class DigestCreateSerializer(serializers.Serializer):
    """Create payload for Digest."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class DigestUpdateSerializer(serializers.Serializer):
    """Partial update for Digest."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class DigestFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

def serialize_notifications_row_0(row: dict) -> dict:
    """Normalize row shape variant 0 for notifications exports."""
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

def serialize_notifications_row_1(row: dict) -> dict:
    """Normalize row shape variant 1 for notifications exports."""
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

def serialize_notifications_row_2(row: dict) -> dict:
    """Normalize row shape variant 2 for notifications exports."""
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

def serialize_notifications_row_3(row: dict) -> dict:
    """Normalize row shape variant 3 for notifications exports."""
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

def serialize_notifications_row_4(row: dict) -> dict:
    """Normalize row shape variant 4 for notifications exports."""
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

def serialize_notifications_row_5(row: dict) -> dict:
    """Normalize row shape variant 5 for notifications exports."""
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

def serialize_notifications_row_6(row: dict) -> dict:
    """Normalize row shape variant 6 for notifications exports."""
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

def serialize_notifications_row_7(row: dict) -> dict:
    """Normalize row shape variant 7 for notifications exports."""
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

def serialize_notifications_row_8(row: dict) -> dict:
    """Normalize row shape variant 8 for notifications exports."""
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

def serialize_notifications_row_9(row: dict) -> dict:
    """Normalize row shape variant 9 for notifications exports."""
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

def serialize_notifications_row_10(row: dict) -> dict:
    """Normalize row shape variant 10 for notifications exports."""
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

def serialize_notifications_row_11(row: dict) -> dict:
    """Normalize row shape variant 11 for notifications exports."""
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

def serialize_notifications_row_12(row: dict) -> dict:
    """Normalize row shape variant 12 for notifications exports."""
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

def serialize_notifications_row_13(row: dict) -> dict:
    """Normalize row shape variant 13 for notifications exports."""
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

def serialize_notifications_row_14(row: dict) -> dict:
    """Normalize row shape variant 14 for notifications exports."""
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
