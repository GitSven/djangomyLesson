from django.contrib import admin
from .models import Category, Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'views')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)