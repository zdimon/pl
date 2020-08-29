from django.contrib import admin

# Register your models here.

from ij.models import *

class CityAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(City, CityAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['publicname']

admin.site.register(UserProfile, UserProfileAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'youdo_id']

admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']

admin.site.register(SubCategory, SubCategoryAdmin)