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
    url(r'^diplomas/(?P<id>[0-9]+)', api.DiplomasUpd.as_view()),
    url(r'^diplomas', api.DiplomasView.as_view()),
    url(r'^logout', api.TokenRenderView.as_view()),
    url(r'^reviewers/(?P<id>[0-9]+)', api.ReviewersUpd.as_view()),
    url(r'^reviewers', api.ReviewersView.as_view()),
    url(r'^guides/(?P<id>[0-9]+)', api.ProfileUpd.as_view()),
    url(r'^guides', api.ProfileView.as_view()),
    url(r'^weeks/(?P<id>[0-9]+)', api.WeekUpd.as_view()),
    url(r'^weeks', api.WeekView.as_view()),
    ]

