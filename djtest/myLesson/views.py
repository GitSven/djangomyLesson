# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
from .forms import Addform


# Create your views here.

# form test
def index(request):
    if request.method == 'POST':

        form = Addform(request.POST)

        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(float(a) + float(b)))
    else:
        form = Addform()
    return render(request, 'mylesson/index.html', {'form': form})


# MTC test
def hello_name(request):
    name = request.GET['name']
    return HttpResponse('hello ' + name)


def hello_nums(request, num1, num2):
    return HttpResponse('hello ' + str(int(num1) + int(num2)))


def hello_tmp(request):
    string = u'离离原上草'
    info_dict = {'title': 'Django 模板学习', 'author': 'sven', 'time': datetime.date(2015, 04, 04)}
    lis = xrange(10)
    return render(request, 'mylesson/tmp.html', {'string': string, 'info_dict': info_dict, 'lis': lis})


def hello_num(request, num):
    return HttpResponse('hello ' + num)


# get test
def getnums(request):
    a = request.GET['a']
    b = request.GET['b']
    return HttpResponse(str(int(a) + int(b)))


# ajax test
from django.http import JsonResponse


def ajax_list(request):
    a = range(100)
    return JsonResponse(a, safe=False)


def ajax_dict(request):
    name_dict = {'twz': 'I Love Py', 'zqxt': 'I am DJJJJ'}
    return JsonResponse(name_dict)


# ajax获取图片
from django.conf import settings
import os
import json

BASE_DIR = settings.BASE_DIR  # 项目目录
# 假设图片放在static/pics/里面
PICS = os.listdir(os.path.join(BASE_DIR, 'common_static/pics'))

print PICS  # 启动时终端上可以看到有哪些图片，我只放了一张，测试完后这一行可以删除


def get_pic(request):
    color = request.GET.get('color')
    number = request.GET.get('number')
    name = '{}_{}'.format(color, number)

    # 过滤出符合要求的图片，假设是以输入的开头的都返回
    result_list = filter(lambda x: x.startswith(name), PICS)

    print 'result_list', result_list

    return HttpResponse(
        json.dumps(result_list),
        content_type='application/json')
