from api.models import Plan, Schedule, UserProfile
from api.serializers import PlanSerializer, ScheduleSerializer, UserSerializer

from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class PlanView(APIView):

    """
    List all plans
    """

    permission_classes = (AllowAny,)

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

    permission_classes = (AllowAny,)

    # checks the plan exists in the database

    # gets the plan

    def get(self, request, planid):
        """
        Retrieve a plan
        """
        plan = get_object_or_404(Plan, pk=planid)
        serializer = PlanSerializer(plan)
        return Response(serializer.data)


# protected view

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


# protected view

class UserPlanDetailView(APIView):

    """
    Retrieve a single userplan and add a single plan to the user
    """

    # get a plan belonging to a user

    def get(self, request, userid, planid):
        """
        Retrieve a plan belonging to the user
        """
        # check that the user exists
        user = get_object_or_404(User, pk=userid)

        plan = Plan.objects.filter(users__id=user.id, pk=planid).get()
        serializer = PlanSerializer(plan)
        return Response(serializer.data)

    # add a plan to a user

    def post(self, request, userid, planid):
        """
        Add a plan to the user's current plans
        """
        plan = get_object_or_404(Plan, pk=planid)
        user = get_object_or_404(User, pk=userid)

        plan.users.add(user)
        return Response(status=status.HTTP_200_OK)


class LoginView(APIView):
    """
    Login a user
    """

    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                if auth_user.is_active:
                    login(request, auth_user)
                    return_data = {
                        'username': serializer.data['username'],
                        'email': serializer.data['email'],
                        'google_id': serializer.data['google_id']
                    }
                    return Response(return_data)
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class LogoutView(APIView):
    """
    Logout a user
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class RegisterView(APIView):
    """
    Register a new user
    """

    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(
                username=request.data['username'],
                password=request.data['password'],
                email=request.data['email']
            )
            auth_user = authenticate(
                username=request.data['username'],
                password=request.data['password']
            )
            login(request, auth_user)
            return_data = {
                'username': serializer.data['username'],
                'email': serializer.data['email'],
            }
            return Response(return_data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
