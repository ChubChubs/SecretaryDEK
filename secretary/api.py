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
from .models import Diploma, Reviewer, UserProfile, HandWeek
from docgen import generator
# from datetime import datetime

'''
    POST /dogs — создать новую собаку
    GET /dogs — получить список собак
    PUT /dogs — редактирование всех собак сразу
    DELETE /dogs — удаление всех собак

    POST /dogs/12345 — вернуть ошибку (собака 12345 уже создана)
    GET /dogs/12345 — показать информацию о собаке
    PUT /dogs/12345 — редактировать собаку 12345
    DELETE /dogs/12345 — удалить
'''


class DiplomaSerializer(serializers.ModelSerializer):
    """
    Data serializer. Simple as shitting bricks.
    """
    class Meta:
        model = Diploma
        fields = ('id', 'theme', 'theme_eng', 'year', 'group', 'reviewer', 'datereview', 'guide', 'guidemark',
                  'pageswork', 'pagespresentation', 'datehanding', 'type', 'fellowship', 'mark', )


class UserSerializer(serializers.ModelSerializer):
    """
    User Model serializer. Secured a little
    """
    class Meta:
        model = User
        fields = ('id', 'username',)

class ReviewerSerializer(serializers.ModelSerializer):
    """
    Reviewer model serializer.
    When the DB will be updated, these shit bricks must change too.
    """
    class Meta:
        model = Reviewer
        fields = ('id', 'name', 'mname', 'surname', )

''
class ProfileSerializer(serializers.ModelSerializer):
    """
    For Profile. Simply. Chunky. Exploitable!
    """
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'mname', 'surname', )

class WeekSerializer(serializers.ModelSerializer):
    """
    For handing weeks.
    """
    class Meta:
        model = HandWeek
        fields = ('id','start', 'finish', 'season')

class DiplomasView(generics.ListCreateAPIView):
    """
    API view for diplomas.
    Handles POST's and GET's
    Handles multiple JSON's
    Shit's JSON's
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Diploma.objects.all()
    serializer_class = DiplomaSerializer
    renderer_classes = (JSONRenderer, )


class DiplomasUpd(generics.RetrieveUpdateDestroyAPIView):
    """
    Additional API view.
    Handles all http requests.
    Handles specified instances, counted by a primary key.
    Does not respond anything.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Diploma.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = DiplomaSerializer
    lookup_field = 'id'


class ExampleView(APIView):
    """
    Example view. Made just for lulz. Usable because does NOT use
    models and authentication.
    """
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        item = generator.gen_a_doc("doc")
        content = {
            "unicode black star": "★",
            "value": 999,
            "method": u"GET",
            "doc": item
        }
        return Response(content)

    def post(self, request, format=None):
        content = {
            "unicode black star": "★",
            "value": "999",
            "method": u"POST"
        }
        return Response(content, status=status.HTTP_202_ACCEPTED)


class TokenRenderView(APIView):
    """
    Logout View. POST!
    Provide your access token, tour login and your password
    To get the hell out of here.
    Basically, makes access token invalid.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            token, _ = Token.objects.get_or_create(
                user=serializer.validated_data['user']
            )
            token.delete()
            token = Token.objects.create(user=serializer.validated_data['user'])
            token.save()
            # data = {'token': token.key} # heh)
            return Response(status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewersView(generics.ListCreateAPIView):
    """
    API for reviewers.
    Handles GET
    :returns:
    All reviewers
    Handles POST
    :returns:
    A JSON with applied data in it.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Reviewer.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = ReviewerSerializer
    lookup_field = 'id'


class ReviewersUpd(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET
    :returns:
    A specified Reviewer.
    Handles PUT.
    It updates a specified Reviewer.
    :returns:
    Noting. Status_200
    Handles DELETE
    Deletes a specified Reviewer
    :returns:
    Nothing
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Reviewer.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = ReviewerSerializer
    lookup_field = 'id'


class ProfileView(generics.ListCreateAPIView):
    """
    API for Profiles.
    Handles GET
    :returns:
    All Profiles
    Handles POST
    :returns:
    A JSON with applied data in it.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = ProfileSerializer
    lookup_field = 'id'


class ProfileUpd(generics.RetrieveUpdateDestroyAPIView):
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
    queryset = UserProfile.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = ProfileSerializer
    lookup_field = 'id'

class WeekView(generics.ListCreateAPIView):
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
    queryset = HandWeek.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = WeekSerializer
    lookup_field = 'id'

class WeekUpd(generics.RetrieveUpdateDestroyAPIView):
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
    queryset = HandWeek.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = WeekSerializer
    lookup_field = 'id'