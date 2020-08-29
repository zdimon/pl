from django.contrib import admin

# Register your models here.

from ij.models import City, UserProfile

class CityAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(City, CityAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['publicname']

admin.site.register(UserProfile, UserProfileAdmin)