import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from bookings.models import Booking
from bookings.services import validate_booking_slot, create_booking, find_conflicts


@pytest.mark.django_db
class TestBookingValidation:
    def test_end_after_start(self, resource, user):
        start = timezone.now() + timedelta(days=1)
        end = start - timedelta(hours=1)
        with pytest.raises(ValidationError):
            validate_booking_slot(resource, start, end, user)

    def test_create_booking_success(self, resource, user):
        start = timezone.now() + timedelta(days=1)
        start = start.replace(hour=10, minute=0, second=0, microsecond=0)
        end = start + timedelta(hours=1)
        booking = create_booking(
            resource=resource,
            user=user,
            title='Team Sync',
            start=start,
            end=end,
        )
        assert booking.pk is not None
        assert booking.status == 'confirmed'
        assert booking.title == 'Team Sync'

    def test_conflict_detection(self, resource, user):
        start = timezone.now() + timedelta(days=2)
        start = start.replace(hour=11, minute=0, second=0, microsecond=0)
        end = start + timedelta(hours=1)
        create_booking(resource=resource, user=user, title='First', start=start, end=end)
        # Overlapping with buffer
        with pytest.raises(ValidationError, match='conflict'):
            create_booking(
                resource=resource,
                user=user,
                title='Second',
                start=start + timedelta(minutes=30),
                end=end + timedelta(minutes=30),
            )

    def test_min_duration(self, resource, user):
        start = timezone.now() + timedelta(days=1)
        start = start.replace(hour=14, minute=0, second=0, microsecond=0)
        end = start + timedelta(minutes=15)  # less than 30
        with pytest.raises(ValidationError, match='Minimum duration'):
            validate_booking_slot(resource, start, end, user)


@pytest.mark.django_db
class TestResource:
    def test_resource_str(self, resource):
        assert str(resource) == 'Conference Room A'

    def test_is_available(self, resource):
        assert resource.is_available is True
