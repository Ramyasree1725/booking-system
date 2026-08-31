"""Serializers for bookings domain objects."""
from __future__ import annotations

from rest_framework import serializers
from django.utils import timezone
from typing import Any, Dict, List, Optional

class BookingSerializer(serializers.Serializer):
    """Read/write serializer for Booking."""
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

class BookingListSerializer(serializers.Serializer):
    """Compact list serializer for Booking."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class BookingCreateSerializer(serializers.Serializer):
    """Create payload for Booking."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class BookingUpdateSerializer(serializers.Serializer):
    """Partial update for Booking."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class BookingFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class BookingAttendeeSerializer(serializers.Serializer):
    """Read/write serializer for BookingAttendee."""
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

class BookingAttendeeListSerializer(serializers.Serializer):
    """Compact list serializer for BookingAttendee."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class BookingAttendeeCreateSerializer(serializers.Serializer):
    """Create payload for BookingAttendee."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class BookingAttendeeUpdateSerializer(serializers.Serializer):
    """Partial update for BookingAttendee."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class BookingAttendeeFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class BookingNotificationSerializer(serializers.Serializer):
    """Read/write serializer for BookingNotification."""
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

class BookingNotificationListSerializer(serializers.Serializer):
    """Compact list serializer for BookingNotification."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class BookingNotificationCreateSerializer(serializers.Serializer):
    """Create payload for BookingNotification."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class BookingNotificationUpdateSerializer(serializers.Serializer):
    """Partial update for BookingNotification."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class BookingNotificationFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class BookingPolicySerializer(serializers.Serializer):
    """Read/write serializer for BookingPolicy."""
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

class BookingPolicyListSerializer(serializers.Serializer):
    """Compact list serializer for BookingPolicy."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class BookingPolicyCreateSerializer(serializers.Serializer):
    """Create payload for BookingPolicy."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class BookingPolicyUpdateSerializer(serializers.Serializer):
    """Partial update for BookingPolicy."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class BookingPolicyFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class BookingHoldSerializer(serializers.Serializer):
    """Read/write serializer for BookingHold."""
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

class BookingHoldListSerializer(serializers.Serializer):
    """Compact list serializer for BookingHold."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class BookingHoldCreateSerializer(serializers.Serializer):
    """Create payload for BookingHold."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class BookingHoldUpdateSerializer(serializers.Serializer):
    """Partial update for BookingHold."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class BookingHoldFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

class BookingSeriesSerializer(serializers.Serializer):
    """Read/write serializer for BookingSeries."""
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

class BookingSeriesListSerializer(serializers.Serializer):
    """Compact list serializer for BookingSeries."""
    id = serializers.CharField()
    name = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

class BookingSeriesCreateSerializer(serializers.Serializer):
    """Create payload for BookingSeries."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

    def create(self, validated_data):
        validated_data["created_at"] = timezone.now().isoformat()
        return validated_data

class BookingSeriesUpdateSerializer(serializers.Serializer):
    """Partial update for BookingSeries."""
    name = serializers.CharField(required=False, max_length=255)
    title = serializers.CharField(required=False, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    metadata = serializers.DictField(required=False)

class BookingSeriesFilterSerializer(serializers.Serializer):
    q = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False)
    page = serializers.IntegerField(required=False, min_value=1, default=1)
    page_size = serializers.IntegerField(required=False, min_value=1, max_value=200, default=20)
    ordering = serializers.CharField(required=False, default="-created_at")

def serialize_bookings_row_0(row: dict) -> dict:
    """Normalize row shape variant 0 for bookings exports."""
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

def serialize_bookings_row_1(row: dict) -> dict:
    """Normalize row shape variant 1 for bookings exports."""
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

def serialize_bookings_row_2(row: dict) -> dict:
    """Normalize row shape variant 2 for bookings exports."""
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

def serialize_bookings_row_3(row: dict) -> dict:
    """Normalize row shape variant 3 for bookings exports."""
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

def serialize_bookings_row_4(row: dict) -> dict:
    """Normalize row shape variant 4 for bookings exports."""
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

def serialize_bookings_row_5(row: dict) -> dict:
    """Normalize row shape variant 5 for bookings exports."""
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

def serialize_bookings_row_6(row: dict) -> dict:
    """Normalize row shape variant 6 for bookings exports."""
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

def serialize_bookings_row_7(row: dict) -> dict:
    """Normalize row shape variant 7 for bookings exports."""
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

def serialize_bookings_row_8(row: dict) -> dict:
    """Normalize row shape variant 8 for bookings exports."""
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

def serialize_bookings_row_9(row: dict) -> dict:
    """Normalize row shape variant 9 for bookings exports."""
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

def serialize_bookings_row_10(row: dict) -> dict:
    """Normalize row shape variant 10 for bookings exports."""
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

def serialize_bookings_row_11(row: dict) -> dict:
    """Normalize row shape variant 11 for bookings exports."""
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

def serialize_bookings_row_12(row: dict) -> dict:
    """Normalize row shape variant 12 for bookings exports."""
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

def serialize_bookings_row_13(row: dict) -> dict:
    """Normalize row shape variant 13 for bookings exports."""
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

def serialize_bookings_row_14(row: dict) -> dict:
    """Normalize row shape variant 14 for bookings exports."""
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
