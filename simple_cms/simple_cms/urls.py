"""simple_cms URL Configuration

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

from news import views as nv

from DjangoUeditor import urls as django_ueditor_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^ueditor/', include(django_ueditor_urls)),

    url(r'^$', nv.index, name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$', nv.column_detail, name='column'),
    url(r'^news/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$', nv.article_detail, name='article'),

]
