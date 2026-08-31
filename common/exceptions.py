
"""Custom API exception hierarchy for consistent error responses."""
from __future__ import annotations

from rest_framework import status
from rest_framework.exceptions import APIException


class BookingAPIException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "A booking error occurred."
    default_code = "booking_error"


class SlotUnavailable(BookingAPIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "The requested time slot is not available."
    default_code = "slot_unavailable"


class SlotConflict(BookingAPIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "This slot conflicts with an existing booking."
    default_code = "slot_conflict"


class OutsideAvailability(BookingAPIException):
    default_detail = "Requested time is outside resource availability hours."
    default_code = "outside_availability"


class BlackoutConflict(BookingAPIException):
    default_detail = "Requested time falls within a blackout period."
    default_code = "blackout_conflict"


class DurationInvalid(BookingAPIException):
    default_detail = "Booking duration is invalid for this resource."
    default_code = "duration_invalid"


class CapacityExceeded(BookingAPIException):
    default_detail = "Attendee count exceeds resource capacity."
    default_code = "capacity_exceeded"


class CancellationNotAllowed(BookingAPIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "This booking cannot be cancelled."
    default_code = "cancellation_not_allowed"


class ApprovalRequired(BookingAPIException):
    status_code = status.HTTP_202_ACCEPTED
    default_detail = "Booking submitted and awaits approval."
    default_code = "approval_required"


class ResourceInactive(BookingAPIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "Resource is not available for booking."
    default_code = "resource_inactive"


class AdvanceWindowExceeded(BookingAPIException):
    default_detail = "Booking is beyond the allowed advance window."
    default_code = "advance_window_exceeded"


class PastBookingNotAllowed(BookingAPIException):
    default_detail = "Cannot create or modify bookings in the past."
    default_code = "past_booking"


class PermissionDeniedDetail(BookingAPIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "You do not have permission to perform this action."
    default_code = "permission_denied"


class RateLimited(BookingAPIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_detail = "Too many requests. Please try again later."
    default_code = "rate_limited"


class IntegrationError(BookingAPIException):
    status_code = status.HTTP_502_BAD_GATEWAY
    default_detail = "Upstream integration failed."
    default_code = "integration_error"


class ExportError(BookingAPIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Failed to generate export."
    default_code = "export_error"


class WebhookDeliveryError(BookingAPIException):
    status_code = status.HTTP_502_BAD_GATEWAY
    default_detail = "Webhook delivery failed."
    default_code = "webhook_delivery_error"


class ValidationAggregate(BookingAPIException):
    """Holds multiple field errors."""

    def __init__(self, errors: dict, detail=None):
        self.errors = errors
        super().__init__(detail=detail or errors)
