"""
Models for farmhands api
"""

from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):

    FARM_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    name = models.CharField(max_length=200)
    farm_size = models.CharField(max_length=30, choices=FARM_SIZES)
    weather = models.CharField(max_length=200)
    crop_type = models.CharField(max_length=200)
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
    google_id = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name='created')
