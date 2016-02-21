"""
Serializers for farmhands
"""

from rest_framework import serializers
from api.models import Plan, Schedule
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    google_id = serializers.CharField(
        source='userprofile.google_id', required=False)
    date_created = serializers.DateTimeField(
        source='userprofile.date_created', required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'google_id', 'date_created')


class PlanSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    schedule = serializers.ReadOnlyField(source='schedule.plan')

    class Meta:
        model = Plan
        fields = (
            'name', 'farm_size', 'weather', 'crop_type', 'budget',
            'duration', 'date_created', 'users',
            'schedule'
        )


class ScheduleSerializer(serializers.ModelSerializer):
    plan = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Schedule
        fields = ('plan', 'start_time', 'end_time', 'cycle_type', 'desc')
