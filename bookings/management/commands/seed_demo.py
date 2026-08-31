
"""Management command: seed demo resources, rules, and sample bookings."""
from __future__ import annotations

from datetime import time, timedelta

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify

from resources.models import Resource, ResourceCategory, AvailabilityRule
from bookings.models import Booking
from bookings.services import create_booking

User = get_user_model()


DEMO_RESOURCES = [
    {"name": "Conference Room A", "capacity": 12, "location": "Floor 2", "amenities": ["TV", "Whiteboard"]},
    {"name": "Conference Room B", "capacity": 8, "location": "Floor 2", "amenities": ["TV"]},
    {"name": "Focus Booth 1", "capacity": 1, "location": "Floor 1", "amenities": ["Desk"]},
    {"name": "Focus Booth 2", "capacity": 1, "location": "Floor 1", "amenities": ["Desk"]},
    {"name": "Training Room", "capacity": 30, "location": "Floor 3", "amenities": ["Projector", "Mic"]},
    {"name": "Board Room", "capacity": 16, "location": "Floor 4", "amenities": ["TV", "Conference Phone"]},
    {"name": "Lab Space", "capacity": 6, "location": "Basement", "amenities": ["Workbench"]},
    {"name": "Interview Room", "capacity": 4, "location": "Floor 1", "amenities": ["Whiteboard"]},
]


class Command(BaseCommand):
    help = "Seed demo categories, resources, availability rules, and sample bookings"

    def add_arguments(self, parser):
        parser.add_argument("--bookings", type=int, default=5, help="Sample bookings to create")
        parser.add_argument("--user", type=str, default="", help="Username to own sample bookings")

    def handle(self, *args, **options):
        cat, _ = ResourceCategory.objects.get_or_create(
            name="Meeting Rooms",
            defaults={"color": "#2563EB", "icon": "door", "order": 1},
        )
        cat2, _ = ResourceCategory.objects.get_or_create(
            name="Focus Spaces",
            defaults={"color": "#059669", "icon": "booth", "order": 2},
        )
        admin = User.objects.filter(is_superuser=True).first()
        created_resources = []
        for i, spec in enumerate(DEMO_RESOURCES):
            slug = slugify(spec["name"])
            category = cat2 if "Booth" in spec["name"] or "Focus" in spec["name"] else cat
            resource, created = Resource.objects.get_or_create(
                slug=slug,
                defaults={
                    "name": spec["name"],
                    "category": category,
                    "capacity": spec["capacity"],
                    "location": spec["location"],
                    "amenities": spec["amenities"],
                    "status": Resource.Status.ACTIVE,
                    "is_public": True,
                    "buffer_minutes": 15,
                    "min_duration_minutes": 30,
                    "max_duration_minutes": 240,
                    "created_by": admin,
                },
            )
            if created:
                for day in range(5):
                    AvailabilityRule.objects.get_or_create(
                        resource=resource,
                        weekday=day,
                        start_time=time(9, 0),
                        end_time=time(18, 0),
                        defaults={"is_active": True},
                    )
                self.stdout.write(self.style.SUCCESS(f"Created resource {resource.name}"))
            created_resources.append(resource)

        username = options["user"]
        user = User.objects.filter(username=username).first() if username else admin
        if user and options["bookings"] > 0 and created_resources:
            base = timezone.now() + timedelta(days=1)
            base = base.replace(hour=10, minute=0, second=0, microsecond=0)
            for i in range(options["bookings"]):
                resource = created_resources[i % len(created_resources)]
                start = base + timedelta(days=i)
                end = start + timedelta(hours=1)
                try:
                    create_booking(
                        resource=resource,
                        user=user,
                        title=f"Demo booking {i + 1}",
                        start=start,
                        end=end,
                        description="Seeded demo booking",
                    )
                    self.stdout.write(f"Created demo booking on {resource.name}")
                except Exception as exc:
                    self.stdout.write(self.style.WARNING(f"Skip booking: {exc}"))

        self.stdout.write(self.style.SUCCESS("Seed complete"))
