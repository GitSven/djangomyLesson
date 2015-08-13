from django.contrib import admin
from .models import Article,Persion
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'content', 'pub_date', 'update_time')

    fields = ['title', 'content']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Persion)