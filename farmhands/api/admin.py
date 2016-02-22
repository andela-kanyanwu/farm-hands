from django.contrib import admin

from .models import Crop, Plan, Schedule, UserProfile


class CropAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Crop Information', {'fields': [
         'climate', 'crop_categories', 'life_cycle', 'price', 'desc']}),
    ]


class ScheduleInline(admin.TabularInline):
    model = Schedule


class PlanAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'crop', 'description']}),
        ('Plan Information', {'fields': [
         'farm_size', 'budget', 'duration']}),
        ('Users', {'fields': ['users']}),
    ]

    inlines = [ScheduleInline]

admin.site.register(Plan, PlanAdmin)
admin.site.register(UserProfile)
admin.site.register(Crop, CropAdmin)
