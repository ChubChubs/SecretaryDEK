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
from django.contrib.auth.decorators import login_required
from secretary import views, urls as APIs
from schedule import urls as SchAPIs


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^$', login_required(views.show_page), name='home'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'base'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='base'), name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),
    url('^diploma/add$', login_required(views.DiplomaCreate.as_view()), name='diploma_add'),
    url(r'^api/', include(APIs)),
    url(r'^api/', include(SchAPIs)),

    # url(r'^api/lol_data', tests.guide_add_data),
]



