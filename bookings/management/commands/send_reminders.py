
"""Send booking reminders for upcoming confirmed bookings."""
from django.core.management.base import BaseCommand
from notifications.services.dispatcher import send_reminders


class Command(BaseCommand):
    help = "Send email reminders for bookings starting within N hours"

    def add_arguments(self, parser):
        parser.add_argument("--hours", type=int, default=24)

    def handle(self, *args, **options):
        sent = send_reminders(within_hours=options["hours"])
        self.stdout.write(self.style.SUCCESS(f"Sent {sent} reminders"))
