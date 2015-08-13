# -*-coding:utf-8-*-

from django.conf.urls import include, url
from .views import *

urlpatterns = [

    url(r'^$', index, name='index'),

    url(r'^getnums$', getnums, name='getnums'),

    url(r'^name$', hello_name, name='hello_name'),
    url(r'^nums/(\d+)\+(\d+)$', hello_nums, name='hello_nums'),
    url(r'^num/(\d+)$', hello_num, name='hello_num'),

    url(r'^tmp$', hello_tmp, name='hello_tmp'),

    url(r'^ajax_list$', ajax_list, name='ajax_list'),
    url(r'^ajax_dict$', ajax_dict, name='ajax_dict'),
    url(r'^get_pic/$', get_pic, name='get_pic'),

]
