# -*- coding:utf-8 -*-

from django.shortcuts import render

from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    category_all = Category.objects.all()
    category_t5 = Category.objects.order_by('-likes')[:5] #-likes,按照likes降序排列
    page_t5 = Page.objects.order_by('-likes')[:5]
    context_dict = {'category_t5': category_t5, 'page_t5':page_t5, 'category_all':category_all}
    return render(request, 'rango/index.html', context_dict)


def category(request,category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request, 'rango/category.html', context_dict)


def about(request):
    return HttpResponse('Rango about!!!<br/><a href="/rango/">index</a>')
