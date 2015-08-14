from django.contrib import admin
from .models import Article, Column
# Register your models here.


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'nav_display', 'idx_display')


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'author', 'publish_time', 'update_time',)

admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)
