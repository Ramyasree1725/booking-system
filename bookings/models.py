from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
import uuid


class Booking(models.Model):
    """A reservation of a resource for a time range."""

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending Approval'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELLED = 'cancelled', 'Cancelled'
        COMPLETED = 'completed', 'Completed'
        REJECTED = 'rejected', 'Rejected'
        NO_SHOW = 'no_show', 'No Show'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resource = models.ForeignKey(
        'resources.Resource', on_delete=models.CASCADE, related_name='bookings',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings',
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_datetime = models.DateTimeField(db_index=True)
    end_datetime = models.DateTimeField(db_index=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.CONFIRMED, db_index=True,
    )
    attendees = models.PositiveIntegerField(default=1)
    is_recurring = models.BooleanField(default=False)
    recurrence_rule = models.CharField(
        max_length=255, blank=True,
        help_text='RRULE string (e.g. FREQ=WEEKLY;COUNT=10)',
    )
    parent_booking = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True,
        related_name='child_bookings',
    )
    cancellation_reason = models.TextField(blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    cancelled_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='cancelled_bookings',
    )
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='approved_bookings',
    )
    approved_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_datetime']
        indexes = [
            models.Index(fields=['resource', 'start_datetime', 'end_datetime']),
            models.Index(fields=['user', 'status']),
            models.Index(fields=['status', 'start_datetime']),
        ]
        # Note: ExclusionConstraint with tstzrange requires PostgreSQL.
        # Applied via migration when using Postgres.
        constraints = [
            models.CheckConstraint(
                check=models.Q(end_datetime__gt=models.F('start_datetime')),
                name='booking_end_after_start',
            ),
        ]

    def __str__(self):
        return f'{self.title} – {self.resource.name} ({self.start_datetime:%Y-%m-%d %H:%M})'

    def clean(self):
        if self.start_datetime and self.end_datetime:
            if self.end_datetime <= self.start_datetime:
                raise ValidationError('End must be after start.')
            duration = (self.end_datetime - self.start_datetime).total_seconds() / 60
            if self.resource_id:
                if duration < self.resource.min_duration_minutes:
                    raise ValidationError(
                        f'Minimum duration is {self.resource.min_duration_minutes} minutes.'
                    )
                if duration > self.resource.max_duration_minutes:
                    raise ValidationError(
                        f'Maximum duration is {self.resource.max_duration_minutes} minutes.'
                    )
            if self.start_datetime < timezone.now() - timedelta(minutes=5):
                raise ValidationError('Cannot book in the past.')

    def can_cancel(self, user):
        if self.status in (self.Status.CANCELLED, self.Status.COMPLETED, self.Status.REJECTED):
            return False
        hours = getattr(settings, 'BOOKING_CANCELLATION_HOURS', 24)
        if self.start_datetime - timezone.now() < timedelta(hours=hours):
            if not (user.is_staff or getattr(user, 'is_admin_role', False)):
                return False
        return self.user_id == user.id or user.is_staff or getattr(user, 'is_admin_role', False)

    def cancel(self, user, reason=''):
        if not self.can_cancel(user):
            raise ValidationError('This booking cannot be cancelled.')
        self.status = self.Status.CANCELLED
        self.cancellation_reason = reason
        self.cancelled_at = timezone.now()
        self.cancelled_by = user
        self.save(update_fields=['status', 'cancellation_reason', 'cancelled_at', 'cancelled_by', 'updated_at'])

    @property
    def duration_minutes(self):
        if self.start_datetime and self.end_datetime:
            return int((self.end_datetime - self.start_datetime).total_seconds() / 60)
        return 0


class BookingAttendee(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='attendee_list')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        null=True, blank=True, related_name='attended_bookings',
    )
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    is_optional = models.BooleanField(default=False)
    response = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')],
        default='pending',
    )

    class Meta:
        unique_together = [('booking', 'user'), ('booking', 'email')]


class BookingNotification(models.Model):
    class NotificationType(models.TextChoices):
        CREATED = 'created', 'Booking Created'
        CONFIRMED = 'confirmed', 'Booking Confirmed'
        CANCELLED = 'cancelled', 'Booking Cancelled'
        REMINDER = 'reminder', 'Reminder'
        APPROVAL_NEEDED = 'approval_needed', 'Approval Needed'
        REJECTED = 'rejected', 'Rejected'

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=30, choices=NotificationType.choices)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(null=True, blank=True)
    is_sent = models.BooleanField(default=False)
    error_message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
