from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class ResourceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text='CSS icon class or emoji')
    color = models.CharField(max_length=7, default='#3B82F6', help_text='Hex color')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Resource categories'

    def __str__(self):
        return self.name


class Resource(models.Model):
    """Bookable room or resource."""

    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        MAINTENANCE = 'maintenance', 'Under Maintenance'
        INACTIVE = 'inactive', 'Inactive'

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        ResourceCategory, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='resources',
    )
    location = models.CharField(max_length=255, blank=True)
    capacity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    amenities = models.JSONField(default=list, blank=True, help_text='List of amenity strings')
    image = models.ImageField(upload_to='resources/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    buffer_minutes = models.PositiveIntegerField(
        default=15,
        help_text='Minimum gap between bookings (minutes)',
    )
    min_duration_minutes = models.PositiveIntegerField(default=30)
    max_duration_minutes = models.PositiveIntegerField(default=480)
    advance_booking_days = models.PositiveIntegerField(
        default=90,
        help_text='How far in advance a booking can be made',
    )
    requires_approval = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, related_name='created_resources',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def is_available(self):
        return self.status == self.Status.ACTIVE


class AvailabilityRule(models.Model):
    """Weekly recurring availability for a resource."""

    class Weekday(models.IntegerChoices):
        MONDAY = 0, 'Monday'
        TUESDAY = 1, 'Tuesday'
        WEDNESDAY = 2, 'Wednesday'
        THURSDAY = 3, 'Thursday'
        FRIDAY = 4, 'Friday'
        SATURDAY = 5, 'Saturday'
        SUNDAY = 6, 'Sunday'

    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='availability_rules')
    weekday = models.IntegerField(choices=Weekday.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['weekday', 'start_time']
        unique_together = [('resource', 'weekday', 'start_time', 'end_time')]

    def __str__(self):
        return f'{self.resource.name} – {self.get_weekday_display()} {self.start_time}-{self.end_time}'

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.start_time >= self.end_time:
            raise ValidationError('start_time must be before end_time')


class BlackoutDate(models.Model):
    """Dates/periods when a resource cannot be booked."""

    resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE,
        related_name='blackouts', null=True, blank=True,
        help_text='Null = applies to all resources',
    )
    title = models.CharField(max_length=200)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reason = models.TextField(blank=True)
    is_recurring_yearly = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['start_datetime']

    def __str__(self):
        target = self.resource.name if self.resource else 'ALL'
        return f'{self.title} ({target})'

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.start_datetime >= self.end_datetime:
            raise ValidationError('start must be before end')
