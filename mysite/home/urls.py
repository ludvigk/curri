"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^subject/(?P<subjectID>[0-9A-Za-z]{6})/$', views.subject, name="subject"),
    url(r'^add_subject/$', views.add_subject, name="add_subject"),
    url(r'^create_subject/$', views.create_subject, name="create_subject"),
    url(r'^subject/(?P<subjectID>[0-9A-Za-z]{6})/$', views.subject, name="subject"),
    url(r'^delete_subject/(?P<subjectID>[0-9A-Za-z]{6})/$',
        views.delete_subject, name="delete_subject"),
    url(r'^add_lecture/(?P<subjectID>[0-9A-Za-z]{6})/$',
        views.add_lecture, name="add_lecture"),
    url(r'^remove_lecture/(?P<subjectID>[0-9A-Za-z]{6})/$',
        views.remove_lecture, name="remove_lecture"),
    url(r'^rate_lecture/$', views.rate_lecture, name="rate_lecture"),
    url(r'^rate_tag/$', views.rate_tag, name="rate_tag"),
    url(r'^add_tag/$', views.add_tag, name="add_tag"),
    url(r'^statistics/(?P<subjectID>[0-9A-Za-z]{6})/$', views.statistics, name='statistics')
]

urlpatterns += staticfiles_urlpatterns()
