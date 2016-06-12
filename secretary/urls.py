__author__ = 'masterbob'
"""
URL's of API's. Kinda close and sturdy.
"""
from django.conf.urls import include, url
from secretary import api
from rest_framework.authtoken import views as rest_views

urlpatterns = [
    url(r'^example', api.ExampleView.as_view()),
    url(r'^login', rest_views.obtain_auth_token),
    url(r'^diploma/(?P<id>[0-9]+)', api.DiplomasUpd.as_view()),
    url(r'^diploma', api.DiplomasView.as_view()),
    url(r'^logout', api.TokenRenderView.as_view()),
    url(r'^reviewer/(?P<id>[0-9]+)', api.ReviewersUpd.as_view()),
    url(r'^reviewer', api.ReviewersView.as_view()),
    url(r'^student/(?P<user>[0-9]+)', api.StudentUpd.as_view()),
    url(r'^student', api.StudentView.as_view()),
    url(r'^chief/(?P<id>[0-9]+)', api.ChiefUpd.as_view()),
    url(r'^chief', api.ChiefView.as_view()),
    url(r'^group/(?P<id>[0-9]+)', api.GroupUpd.as_view()),
    url(r'^group', api.GroupView.as_view()),
    url(r'^studrestrict/(?P<id>[0-9]+)', api.StudentsRestrictionsUpd.as_view()),
    url(r'^studrestrict', api.StudentsRestrictionsView.as_view()),
    url(r'^commission/(?P<user>[0-9]+)', api.CommissionUpd.as_view()),
    url(r'^commission', api.CommissiontView.as_view()),
    url(r'^general/(?P<id>[0-9]+)', api.GeneralUpd.as_view()),
    url(r'^general', api.GeneralView.as_view()),
    url(r'^user/(?P<id>[0-9]+)', api.UsersUpd.as_view()),
    url(r'^user', api.UsersView.as_view()),
    ]

