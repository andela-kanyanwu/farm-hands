"""
Serializers for farmhands
"""

from rest_framework import serializers
from api.models import Plan, Schedule
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    google_id = serializers.CharField(source='userprofile.google_id')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'google_id', 'created_at')


class PlanSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    schedule = serializers.ReadOnlyField(source='schedule.plan')

    class Meta:
        model = Plan
        fields = (
            'name', 'farm_size', 'weather', 'crop_type', 'budget',
            'duration', 'date_created', 'auto_now_add', 'users',
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
