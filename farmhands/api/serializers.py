from rest_framework import serializers
from api.models import Plan, Schedule, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('user', 'google_id', 'created_at')


class PlanSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Plan
        fields = ('name', 'farm_size', 'weather', 'crop_type', 'budget',
                  'duration', 'date_created', 'auto_now_add', 'users')


class ScheduleSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()

    class Meta:
        model = Schedule
        fields = ('plan', 'start_time', 'end_time', 'cycle_type', 'desc')
