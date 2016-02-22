"""
Serializers for farmhands
"""

from rest_framework import serializers
from api.models import Plan, Schedule, Crop
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    google_id = serializers.CharField(
        source='userprofile.google_id', required=False)
    date_created = serializers.DateTimeField(
        source='userprofile.date_created', required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'google_id', 'date_created')
        extra_kwargs = {'password': {'write_only': True}}


class CropSerializer(serializers.ModelSerializer):
    plan = serializers.ReadOnlyField(source='plan.crop')

    class Meta:
        model = Crop
        fields = (
            'name', 'climate', 'crop_categories', 'life_cycle',
            'price', 'desc', 'date_created',
            'plan'
        )


class PlanSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    schedule = serializers.ReadOnlyField(source='schedule.plan')
    crop = CropSerializer(read_only=True)

    class Meta:
        model = Plan
        fields = (
            'id', 'name', 'farm_size', 'crop', 'budget',
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
