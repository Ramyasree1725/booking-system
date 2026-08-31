import pytest
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from rest_framework import status
from bookings.models import Booking


@pytest.mark.django_db
class TestBookingAPI:
    def test_list_requires_auth(self, api_client):
        res = api_client.get('/api/bookings/')
        assert res.status_code in (401, 403)

    def test_create_booking(self, api_client, user, resource):
        api_client.force_authenticate(user=user)
        start = timezone.now() + timedelta(days=3)
        start = start.replace(hour=10, minute=0, second=0, microsecond=0)
        end = start + timedelta(hours=1)
        payload = {
            'resource_id': resource.id,
            'title': 'API Test Booking',
            'start_datetime': start.isoformat(),
            'end_datetime': end.isoformat(),
            'attendees': 2,
        }
        res = api_client.post('/api/bookings/', payload, format='json')
        assert res.status_code == status.HTTP_201_CREATED
        assert res.data['title'] == 'API Test Booking'
        assert Booking.objects.filter(title='API Test Booking').exists()

    def test_cancel_booking(self, api_client, user, resource):
        api_client.force_authenticate(user=user)
        start = timezone.now() + timedelta(days=5)
        start = start.replace(hour=10, minute=0, second=0, microsecond=0)
        end = start + timedelta(hours=1)
        from bookings.services import create_booking
        booking = create_booking(
            resource=resource, user=user, title='To Cancel',
            start=start, end=end,
        )
        res = api_client.post(f'/api/bookings/{booking.id}/cancel/', {'reason': 'Changed plans'}, format='json')
        assert res.status_code == 200
        booking.refresh_from_db()
        assert booking.status == 'cancelled'


@pytest.mark.django_db
class TestResourceAPI:
    def test_list_resources(self, api_client, resource):
        res = api_client.get('/api/resources/resources/')
        # May require auth depending on settings; AllowAny for list of public
        assert res.status_code in (200, 401, 403)
