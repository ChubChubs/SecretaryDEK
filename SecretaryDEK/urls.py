"""SecretaryDEK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from secretary import views, urls as APIs

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.show_base, name='base'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'base'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='base'), name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),
    url(r'^api/', include(APIs)),

    # url(r'^api/lol_data', tests.guide_add_data),
]


