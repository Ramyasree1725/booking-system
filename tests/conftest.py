import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from resources.models import Resource, ResourceCategory, AvailabilityRule
from datetime import time

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123',
        role='user',
    )


@pytest.fixture
def admin_user(db):
    return User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='adminpass123',
        role='admin',
    )


@pytest.fixture
def category(db):
    return ResourceCategory.objects.create(name='Meeting Rooms', color='#3B82F6')


@pytest.fixture
def resource(db, category, admin_user):
    r = Resource.objects.create(
        name='Conference Room A',
        slug='conference-room-a',
        category=category,
        capacity=10,
        location='Floor 2',
        buffer_minutes=15,
        min_duration_minutes=30,
        max_duration_minutes=240,
        created_by=admin_user,
        status='active',
        is_public=True,
    )
    for day in range(5):  # Mon-Fri
        AvailabilityRule.objects.create(
            resource=r,
            weekday=day,
            start_time=time(9, 0),
            end_time=time(18, 0),
        )
    return r
