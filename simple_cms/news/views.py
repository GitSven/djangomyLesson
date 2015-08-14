# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article, Column


# Create your views here.


def index(request):
    idx_display_columns = Column.objects.filter(idx_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
    return render(request, 'index.html',
                  {'idx_display_columns': idx_display_columns,
                   'nav_display_columns': nav_display_columns,
                   })


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column': column})


def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)

    if article_slug != article.slug:
        return redirect(article, permanent=True)

    return render(request, 'news/article.html', {'article': article})
