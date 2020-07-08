from django.contrib import admin
from index.models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    search_fields = ['title']