from django.contrib import admin
from .models import Booking, BookingAttendee, BookingNotification


class AttendeeInline(admin.TabularInline):
    model = BookingAttendee
    extra = 0


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'resource', 'user', 'start_datetime', 'end_datetime',
        'status', 'attendees', 'created_at',
    )
    list_filter = ('status', 'resource', 'is_recurring', 'start_datetime')
    search_fields = ('title', 'description', 'user__username', 'user__email')
    readonly_fields = ('id', 'created_at', 'updated_at', 'cancelled_at', 'approved_at')
    inlines = [AttendeeInline]
    date_hierarchy = 'start_datetime'
    raw_id_fields = ('user', 'resource', 'cancelled_by', 'approved_by', 'parent_booking')


@admin.register(BookingNotification)
class BookingNotificationAdmin(admin.ModelAdmin):
    list_display = ('booking', 'notification_type', 'recipient', 'is_sent', 'sent_at', 'created_at')
    list_filter = ('notification_type', 'is_sent')
    readonly_fields = ('created_at',)
