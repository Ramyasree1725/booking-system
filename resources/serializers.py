from rest_framework import serializers
from .models import ResourceCategory, Resource, AvailabilityRule, BlackoutDate


class ResourceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceCategory
        fields = ('id', 'name', 'description', 'icon', 'color', 'order', 'is_active')


class AvailabilityRuleSerializer(serializers.ModelSerializer):
    weekday_display = serializers.CharField(source='get_weekday_display', read_only=True)

    class Meta:
        model = AvailabilityRule
        fields = ('id', 'resource', 'weekday', 'weekday_display', 'start_time', 'end_time', 'is_active')
        read_only_fields = ('id',)


class BlackoutDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackoutDate
        fields = (
            'id', 'resource', 'title', 'start_datetime', 'end_datetime',
            'reason', 'is_recurring_yearly', 'created_at',
        )
        read_only_fields = ('id', 'created_at')


class ResourceSerializer(serializers.ModelSerializer):
    category_detail = ResourceCategorySerializer(source='category', read_only=True)
    availability_rules = AvailabilityRuleSerializer(many=True, read_only=True)
    is_available = serializers.BooleanField(read_only=True)

    class Meta:
        model = Resource
        fields = (
            'id', 'name', 'slug', 'description', 'category', 'category_detail',
            'location', 'capacity', 'amenities', 'image', 'status',
            'buffer_minutes', 'min_duration_minutes', 'max_duration_minutes',
            'advance_booking_days', 'requires_approval', 'is_public',
            'metadata', 'availability_rules', 'is_available',
            'created_at', 'updated_at',
        )
        read_only_fields = ('id', 'slug', 'created_at', 'updated_at')


class ResourceListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True, default=None)

    class Meta:
        model = Resource
        fields = (
            'id', 'name', 'slug', 'location', 'capacity', 'status',
            'category_name', 'buffer_minutes', 'is_public', 'image',
        )
