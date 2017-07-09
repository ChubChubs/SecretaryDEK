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
from .models import Diploma, Reviewer, Student, StudentsRestriction, Commission, Chief, General, Group
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
class StudentsRestictionSerializer(serializers.ModelSerializer):
    """
    Serializer for Groups
    """
    class Meta:
        model = Group
        fields = ( 'chief', 'numberofstudents', 'handingperiod')


class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer for Groups
    """
    class Meta:
        model = Group
        fields = ( 'name' , 'spec')


class CommissionSerilizer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Commission
        fields = ( 'handingday', 'chairman', 'commissioner1', 'commissioner2', 'ommissioner3',
                  'commissioner4', 'commissioner5' ,)

class ChiefSerializer(serializers.ModelSerializer):
    """
    Serializer for Chiefs.
    """
    class Meta:
        model = Chief
        fields = ( 'user', 'education', 'special_education', 'academic_status', 'degree', 'position')

class GeneralSerializer(serializers.ModelSerializer):
    """
    Serializer for General data in user profiles
    """
    class Meta:
        model = General
        fields = ('user', 'bdate', 'mname', 'home', 'passseries', 'passnum', 'passplace' , 'passdate', 'idnum',
                  'registered',)

class DiplomaSerializer(serializers.ModelSerializer):
    """
    Data serializer. Simple as shitting bricks.
    """
    class Meta:
        model = Diploma
        fields = ('theme', 'theme_eng', 'group', 'reviewer', 'datereview', 'chief', 'chiefmark',
                  'numberofpages', 'numberofslides', 'handingdate', 'type', 'fellowship', 'commissionmark', )


class UserSerializer(serializers.ModelSerializer):
    """
    User Model serializer. Secured a little
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class ReviewerSerializer(serializers.ModelSerializer):
    """
    Reviewer model serializer.
    When the DB will be updated, these shit bricks must change too.
    """
    class Meta:
        model = Reviewer
        fields = ( 'user', 'children', 'education', 'special_education', 'academic_status', 'degree', 'position', 'workplace')

class StudentSerializer(serializers.ModelSerializer):
    """
    For Profile. Simply. Chunky. Exploitable!
    """
    class Meta:
        model = Student
        fields = ( 'user', 'entry2uni', 'group', )



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
        #item = generator.gen_a_doc("barchelor_list")
        item = generator.gen_many_docs("phd_direction")
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


class StudentView(generics.ListCreateAPIView):
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
    queryset = Student.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = StudentSerializer
    lookup_field = 'user'


class StudentUpd(generics.RetrieveUpdateDestroyAPIView):
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
    queryset = Student.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = StudentSerializer
    lookup_field = 'user'


class ChiefView(generics.ListCreateAPIView):
    """
    API for Chief.
    Handles GET
    :returns:
    All Profiles
    Handles POST
    :returns:
    A JSON with applied data in it.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Chief.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = ChiefSerializer
    lookup_field = 'id'


class ChiefUpd(generics.RetrieveUpdateDestroyAPIView):
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
    queryset = Chief.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = ChiefSerializer
    lookup_field = 'id'


class GeneralView(generics.ListCreateAPIView):
    """
    API for Profiles.
    Handles GET
    :returns:
    All Profiles
    Handles POST
    :returns:
    A JSON with applied data in it.
    """
    authentication_classes = ( BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = General.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = GeneralSerializer
    lookup_field = 'user'


class GeneralUpd(generics.RetrieveUpdateDestroyAPIView):
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
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser, IsAdminUser)
    queryset = General.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = GeneralSerializer
    lookup_field = 'user'


class CommissiontView(generics.ListCreateAPIView):
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
    queryset = Commission.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = CommissionSerilizer
    lookup_field = 'id'


class CommissionUpd(generics.RetrieveUpdateDestroyAPIView):
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
    queryset = Commission.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = CommissionSerilizer
    lookup_field = 'id'

class GroupView(generics.ListCreateAPIView):
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
    queryset = Group.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = GroupSerializer
    lookup_field = 'id'


class GroupUpd(generics.RetrieveUpdateDestroyAPIView):
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
    queryset = Group.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = GroupSerializer
    lookup_field = 'id'


class StudentsRestrictionsView(generics.ListCreateAPIView):
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
    queryset = StudentsRestriction.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = StudentsRestictionSerializer
    lookup_field = 'id'


class StudentsRestrictionsUpd(generics.RetrieveUpdateDestroyAPIView):
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
    queryset = StudentsRestriction.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = StudentsRestictionSerializer
    lookup_field = 'id'


class UsersView(generics.ListCreateAPIView):
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
    queryset = User.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = UserSerializer
    lookup_field = 'id'


class UsersUpd(generics.RetrieveUpdateDestroyAPIView):
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
    queryset = User.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = UserSerializer
    lookup_field = 'id'

