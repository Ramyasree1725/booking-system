
"""Purge old cancelled/completed bookings and audit logs."""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

from bookings.models import Booking


class Command(BaseCommand):
    help = "Delete old cancelled/completed bookings"

    def add_arguments(self, parser):
        parser.add_argument("--days", type=int, default=365)
        parser.add_argument("--dry-run", action="store_true")

    def handle(self, *args, **options):
        cutoff = timezone.now() - timedelta(days=options["days"])
        qs = Booking.objects.filter(
            status__in=[Booking.Status.CANCELLED, Booking.Status.COMPLETED, Booking.Status.REJECTED],
            end_datetime__lt=cutoff,
        )
        count = qs.count()
        if options["dry_run"]:
            self.stdout.write(f"Would delete {count} bookings")
            return
        deleted, _ = qs.delete()
        self.stdout.write(self.style.SUCCESS(f"Deleted {deleted} bookings"))
