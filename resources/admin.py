from django.contrib import admin
from .models import ResourceCategory, Resource, AvailabilityRule, BlackoutDate


class AvailabilityRuleInline(admin.TabularInline):
    model = AvailabilityRule
    extra = 1


class BlackoutInline(admin.TabularInline):
    model = BlackoutDate
    extra = 0
    fk_name = 'resource'


@admin.register(ResourceCategory)
class ResourceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active', 'color')
    list_editable = ('order', 'is_active')
    search_fields = ('name',)


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'location', 'capacity', 'status', 'buffer_minutes', 'is_public')
    list_filter = ('status', 'category', 'is_public', 'requires_approval')
    search_fields = ('name', 'slug', 'location', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [AvailabilityRuleInline, BlackoutInline]
    readonly_fields = ('created_at', 'updated_at')


@admin.register(AvailabilityRule)
class AvailabilityRuleAdmin(admin.ModelAdmin):
    list_display = ('resource', 'weekday', 'start_time', 'end_time', 'is_active')
    list_filter = ('weekday', 'is_active', 'resource')


@admin.register(BlackoutDate)
class BlackoutDateAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource', 'start_datetime', 'end_datetime', 'is_recurring_yearly')
    list_filter = ('is_recurring_yearly', 'resource')
    search_fields = ('title', 'reason')
