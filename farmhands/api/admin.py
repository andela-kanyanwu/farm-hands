from django.contrib import admin

from .models import Plan, Schedule, UserProfile


class ScheduleInline(admin.TabularInline):
    model = Schedule


class PlanAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Plan Information', {'fields': [
         'farm_size', 'weather',
         'crop_type', 'budget', 'duration']}),
        ('Users', {'fields': ['users']}),
    ]

    inlines = [ScheduleInline]

admin.site.register(Plan, PlanAdmin)
admin.site.register(UserProfile)
