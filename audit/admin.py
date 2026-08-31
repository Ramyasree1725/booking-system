from django.contrib import admin
from .models import AuditLog, AuditRetentionPolicy

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ("action", "content_type", "object_id", "actor_username", "created_at")
    list_filter = ("action", "content_type")
    search_fields = ("object_id", "actor_username", "object_repr", "request_id")
    readonly_fields = [f.name for f in AuditLog._meta.fields]
    date_hierarchy = "created_at"

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(AuditRetentionPolicy)
class AuditRetentionPolicyAdmin(admin.ModelAdmin):
    list_display = ("name", "retain_days", "is_active")
