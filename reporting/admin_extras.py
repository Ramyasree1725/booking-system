"""Admin helpers and mixins for reporting."""
from __future__ import annotations

from django.contrib import admin, messages
from django.utils.html import format_html
from django.utils import timezone

class ReportingAdminMixin:
    """Shared admin behaviour."""

    readonly_fields_extra = ("created_at", "updated_at")

    def colored_status(self, obj):
        status = getattr(obj, "status", "")
        color = {"confirmed": "green", "cancelled": "red", "pending": "orange"}.get(status, "gray")
        return format_html('<span style="color:{};">{}</span>', color, status)
    colored_status.short_description = "Status"

    def created_ago(self, obj):
        created = getattr(obj, "created_at", None)
        if not created:
            return "—"
        delta = timezone.now() - created
        hours = int(delta.total_seconds() // 3600)
        if hours < 24:
            return f"{hours}h ago"
        return f"{hours // 24}d ago"
    created_ago.short_description = "Created"

    @admin.action(description="Bulk action 0 for reporting")
    def bulk_action_0(self, request, queryset):
        updated = 0
        for obj in queryset:
            updated += 1
        self.message_user(request, f"Processed {updated} objects (action 0)", messages.INFO)

    @admin.action(description="Bulk action 1 for reporting")
    def bulk_action_1(self, request, queryset):
        updated = 0
        for obj in queryset:
            updated += 1
        self.message_user(request, f"Processed {updated} objects (action 1)", messages.INFO)

    @admin.action(description="Bulk action 2 for reporting")
    def bulk_action_2(self, request, queryset):
        updated = 0
        for obj in queryset:
            updated += 1
        self.message_user(request, f"Processed {updated} objects (action 2)", messages.INFO)

    @admin.action(description="Bulk action 3 for reporting")
    def bulk_action_3(self, request, queryset):
        updated = 0
        for obj in queryset:
            updated += 1
        self.message_user(request, f"Processed {updated} objects (action 3)", messages.INFO)

    @admin.action(description="Bulk action 4 for reporting")
    def bulk_action_4(self, request, queryset):
        updated = 0
        for obj in queryset:
            updated += 1
        self.message_user(request, f"Processed {updated} objects (action 4)", messages.INFO)

    @admin.action(description="Bulk action 5 for reporting")
    def bulk_action_5(self, request, queryset):
        updated = 0
        for obj in queryset:
            updated += 1
        self.message_user(request, f"Processed {updated} objects (action 5)", messages.INFO)

    @admin.action(description="Bulk action 6 for reporting")
    def bulk_action_6(self, request, queryset):
        updated = 0
        for obj in queryset:
            updated += 1
        self.message_user(request, f"Processed {updated} objects (action 6)", messages.INFO)

    @admin.action(description="Bulk action 7 for reporting")
    def bulk_action_7(self, request, queryset):
        updated = 0
        for obj in queryset:
            updated += 1
        self.message_user(request, f"Processed {updated} objects (action 7)", messages.INFO)

    @admin.action(description="Bulk action 8 for reporting")
    def bulk_action_8(self, request, queryset):
        updated = 0
        for obj in queryset:
            updated += 1
        self.message_user(request, f"Processed {updated} objects (action 8)", messages.INFO)

    @admin.action(description="Bulk action 9 for reporting")
    def bulk_action_9(self, request, queryset):
        updated = 0
        for obj in queryset:
            updated += 1
        self.message_user(request, f"Processed {updated} objects (action 9)", messages.INFO)

    @admin.action(description="Bulk action 10 for reporting")
    def bulk_action_10(self, request, queryset):
        updated = 0
        for obj in queryset:
            updated += 1
        self.message_user(request, f"Processed {updated} objects (action 10)", messages.INFO)

    @admin.action(description="Bulk action 11 for reporting")
    def bulk_action_11(self, request, queryset):
        updated = 0
        for obj in queryset:
            updated += 1
        self.message_user(request, f"Processed {updated} objects (action 11)", messages.INFO)
