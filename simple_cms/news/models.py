# -*- coding:utf-8 -*-

# Create your models here.
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

from DjangoUeditor.models import UEditorField


@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('栏目名称', max_length=255)
    slug = models.CharField('栏目网址', max_length=255, db_index=True)
    intro = models.TextField('栏目简介', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('column', args=(self.slug,))


@python_2_unicode_compatible
class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')

    title = models.CharField('标题', max_length=255)
    slug = models.CharField('网址', max_length=255, db_index=True)

    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
    content = UEditorField('内容', height=300, width=800, default=u'', blank=True,
                           imagePath='upload/imgs/', toolbars='besttome', filePath='upload/files'
                           )

    published = models.BooleanField('正式发布', default=True)

    publish_time = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻'

    def get_absolute_url(self):
        return reverse('article', args=(self.slug,))
