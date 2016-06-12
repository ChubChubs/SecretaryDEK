__author__ = 'masterbob'
from .models import HandingDay, HandingPeriod
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics
from rest_framework import serializers
from rest_framework.authtoken.views import AuthTokenSerializer,ObtainAuthToken
from rest_framework.authtoken.models import Token

class HandingPeriodSerializer(serializers.ModelSerializer):
    """
    For handing weeks.
    """
    class Meta:
        model = HandingPeriod
        fields = ('start', 'end')


class HandingDaySerializer(serializers.ModelSerializer):
    """
    For handing weeks.
    """
    class Meta:
        model = HandingDay
        fields = ('period','date', 'start_time', 'end_time')




class HandingPeriodView(generics.ListCreateAPIView):
    """
    API for handling weeks.
    Handles GET
    :returns:
    All weeks.
    Handles POST
    :returns:
    A JSON with applied data in it.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = HandingPeriod.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = HandingPeriodSerializer
    lookup_field = 'id'

class HandingPeriodUpd(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET
    :returns:
    A specified Profile.
    Handles PUT.
    It updates a specified Profile.
    :returns:
    Noting. Status_200
    Handles DELETE
    Deletes a specified Profile
    :returns:
    Nothing
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser, IsAdminUser)
    queryset = HandingPeriod.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = HandingPeriodSerializer
    lookup_field = 'id'


class HandingDayView(generics.ListCreateAPIView):
    """
    API for handling weeks.
    Handles GET
    :returns:
    All weeks.
    Handles POST
    :returns:
    A JSON with applied data in it.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = HandingPeriod.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = HandingDaySerializer
    lookup_field = 'id'

class HandingDayUpd(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET
    :returns:
    A specified Profile.
    Handles PUT.
    It updates a specified Profile.
    :returns:
    Noting. Status_200
    Handles DELETE
    Deletes a specified Profile
    :returns:
    Nothing
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser, IsAdminUser)
    queryset = HandingPeriod.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = HandingDaySerializer
    lookup_field = 'id'