# -*- coding:utf-8 -*-

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect

from .models import *
from .forms import *
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


def add_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    return render(request, 'rango/add_catrgory.html', {'form': form})


def add_page(request, category_name_slug):

    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
                cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.save()
                # probably better to use a redirect here.
                return redirect('/rango/category/'+cat.slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form': form, 'category': cat}

    return render(request, 'rango/add_page.html', context_dict)
