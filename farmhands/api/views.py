from api.models import Plan, Schedule, UserProfile
from api.serializers import PlanSerializer, ScheduleSerializer, UserSerializer

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PlanView(APIView):

    """
    List all plans
    """

    # gets all plans from the database

    def get(self, request):
        """
        List all plans
        """
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data)


class PlanDetailView(APIView):

    """
    Retrieve a single detailed plan
    """

    # checks the plan exists in the database

    # gets the plan

    def get(self, request, planid):
        """
        Retrieve a plan
        """
        plan = get_object_or_404(Plan, pk=planid)
        serializer = PlanSerializer(plan)
        return Response(serializer.data)


class UserPlanView(APIView):

    """
    Retrieve all User Plans
    """

    # get all plans belonging to the user

    def get(self, request, userid):
        """
        Retrieve all plans belonging to the user
        """

        # check that the user exists
        user = get_object_or_404(User, pk=userid)

        plans = Plan.objects.filter(users__id=user.id)
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data)


class UserPlanDetailView(APIView):

    """
    Retrieve a single userplan
    """

    # get a plan belonging to a user

    def get(self, request, userid, planid):
        """
        Retrieve a plan belonging to the user
        """

        # check that the user exists
        user = get_object_or_404(User, pk=userid)

        plan = Plan.objects.filter(users__id=user.id, pk=planid)
        serializer = PlanSerializer(plan)
        return Response(serializer.data)

