"""
Models for farmhands api
"""

from django.db import models
from django.contrib.auth.models import User


class Crop(models.Model):

    CLIMATE = (
        ('W', 'Tropical Wet'),
        ('MO', 'Monsoon'),
        ('S', 'Savanna'),
        ('A', 'Arid'),
        ('SA', 'Semi Arid'),
        ('ME', 'Mediterranean'),
        ('HS', 'Humid Subtropical'),
        ('MA', 'Marine'),
        ('WS', 'Warm Summer'),
        ('CS', 'Cool Summer'),
        ('B', 'Boreal'),
        ('T', 'Tundra'),
        ('I', 'Ice cap'),
    )

    LIFE_CYCLE = (
        ('ANNUAL', 'Annual'),
        ('BIENNAL', 'Biennal'),
        ('PERENNIAL', 'Perennial'),
        ('EPHEMERALS', 'Ephemerals'),
    )

    CROP_CATEGORIES = (
        ('FOOD', 'Food'),
        ('FEED', 'Feed'),
        ('FIBRE', 'Fibre'),
        ('OIL', 'Oil'),
        ('ORNAMENTAL', 'Ornamental'),
        ('INDUSTRIAL', 'Industrial'),
    )

    name = models.CharField(max_length=200)
    climate = models.CharField(max_length=30, choices=CLIMATE)
    crop_categories = models.CharField(max_length=30, choices=CROP_CATEGORIES)
    life_cycle = models.CharField(max_length=30, choices=LIFE_CYCLE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    desc = models.CharField(max_length=200)
    date_created = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name='created')


class Plan(models.Model):

    FARM_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    name = models.CharField(max_length=200)
    crop = models.ForeignKey(Crop, related_name='plan')
    farm_size = models.CharField(max_length=30, choices=FARM_SIZES)
    budget = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.IntegerField(default=0)
    date_created = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name='created')
    users = models.ManyToManyField(User, blank=True)


class Schedule(models.Model):

    CYCLE_TYPE = (
        ('DAILY', 'daily'),
        ('BIWEEKLY', 'biweekly'),
        ('MONTHLY', 'monthly'),
        ('YEARLY', 'yearly'),
    )

    plan = models.ForeignKey(Plan, related_name='schedule')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cycle_type = models.CharField(max_length=30, choices=CYCLE_TYPE)
    desc = models.CharField(max_length=200)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    google_id = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name='created')
