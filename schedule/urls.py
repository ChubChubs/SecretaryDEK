
__author__ = 'masterbob'
"""
URL's of API's. Kinda close and sturdy.
"""
from django.conf.urls import include, url
from schedule import api
from rest_framework.authtoken import views as rest_views

urlpatterns = [
    url(r'^handper/(?P<id>[0-9]+)', api.HandingPeriodUpd.as_view()),
    url(r'^handper', api.HandingPeriodView.as_view()),
    url(r'^handday/(?P<id>[0-9]+)', api.HandingDayUpd.as_view()),
    url(r'^handday', api.HandingDayView.as_view()),
    ]