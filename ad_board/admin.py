# -*- coding: utf-8 -*-
# Register your models here.
from django.contrib import admin

from ad_board.models.models import Advertisement, Category


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'date_published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', 'price', 'date_published')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Category, CategoryAdmin)