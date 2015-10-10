from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
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
from .models import Diploma
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
        fields = ('theme', 'theme_eng', 'year', 'group', 'reviewer', 'datereview', 'guide', 'guidemark', 'pageswork',
                  'pagespresentation', 'datehanding', 'type', 'fellowship', 'mark', )


class DiplomaView(generics.ListCreateAPIView):
    """
    API view for diplomas.
    Handles POST's and GET's
    Handles multiple JSON's
    Shit's JSON's
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Diploma.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = DiplomaSerializer


class ExampleView(APIView):
    """
    Example view. Made just for lulz. Usable because does NOT use
    models and authentication.
    """
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        content = {
            "unicode black star": "★",
            "value": 999,
            "method": u"GET"
        }
        return Response(content)

    def post(self, request, format=None):
        content = {
            "unicode black star": "★",
            "value": "999",
            "method": u"POST"
        }
        return Response(content, status=status.HTTP_202_ACCEPTED)


class UserView(generics.ListAPIView, mixins.ListModelMixin,
               mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
        """
        User view API.
        Has to handle full spectre of requests. User-friendly.
        Has many things todo. What todo is listed below. If not, then it's done!)
        """
        # TODO: Authentication,Session and Tokenizing all the way
        # TODO: GET, POST, PUT and DELETE
        # TODO: Validation
        # TODO: Consider a split to a few API's
        queryset = User.objects.all()
        renderer_classes = (JSONRenderer, )
        serializer_class = serializers.Serializer

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
            data = {'token': token.key} # heh)
            return Response(status.HTTP_200_OK)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
