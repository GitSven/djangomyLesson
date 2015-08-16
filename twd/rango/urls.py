# -*-coding:utf-8-*-

from django.conf.urls import url, patterns
from rango.views import *

urlpatterns = patterns('',
      url(r'^$', index, name='index'),
      url(r'^about/', about, name='about'),
      url(r'^category/(?P<category_name_slug>[\w\-]+)/$', category, name='category')

)
