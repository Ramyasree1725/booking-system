from rest_framework import serializers
from django.utils import timezone
from resources.serializers import ResourceListSerializer
from accounts.serializers import UserSerializer
from .models import Booking, BookingAttendee
from .services import create_booking, validate_booking_slot


class BookingAttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingAttendee
        fields = ('id', 'user', 'name', 'email', 'is_optional', 'response')


class BookingSerializer(serializers.ModelSerializer):
    resource_detail = ResourceListSerializer(source='resource', read_only=True)
    user_detail = UserSerializer(source='user', read_only=True)
    duration_minutes = serializers.IntegerField(read_only=True)
    can_cancel = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = (
            'id', 'resource', 'resource_detail', 'user', 'user_detail',
            'title', 'description', 'start_datetime', 'end_datetime',
            'status', 'attendees', 'is_recurring', 'recurrence_rule',
            'parent_booking', 'cancellation_reason', 'cancelled_at',
            'notes', 'metadata', 'duration_minutes', 'can_cancel',
            'created_at', 'updated_at',
        )
        read_only_fields = (
            'id', 'user', 'status', 'cancelled_at', 'cancellation_reason',
            'created_at', 'updated_at',
        )

    def get_can_cancel(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.can_cancel(request.user)
        return False


class BookingCreateSerializer(serializers.Serializer):
    resource_id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(required=False, allow_blank=True, default='')
    start_datetime = serializers.DateTimeField()
    end_datetime = serializers.DateTimeField()
    attendees = serializers.IntegerField(min_value=1, default=1)
    notes = serializers.CharField(required=False, allow_blank=True, default='')

    def validate(self, attrs):
        from resources.models import Resource
        try:
            resource = Resource.objects.get(pk=attrs['resource_id'])
        except Resource.DoesNotExist:
            raise serializers.ValidationError({'resource_id': 'Resource not found.'})
        attrs['resource'] = resource
        validate_booking_slot(
            resource,
            attrs['start_datetime'],
            attrs['end_datetime'],
            self.context['request'].user,
        )
        return attrs

    def create(self, validated_data):
        resource = validated_data.pop('resource')
        validated_data.pop('resource_id', None)
        user = self.context['request'].user
        booking = create_booking(
            resource=resource,
            user=user,
            title=validated_data['title'],
            start=validated_data['start_datetime'],
            end=validated_data['end_datetime'],
            description=validated_data.get('description', ''),
            attendees=validated_data.get('attendees', 1),
            metadata={'notes': validated_data.get('notes', '')},
        )
        return booking


class BookingCancelSerializer(serializers.Serializer):
    reason = serializers.CharField(required=False, allow_blank=True, default='')
