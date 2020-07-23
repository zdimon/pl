from django.contrib import admin

from .models import UserProfile, Promocode

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['publicname']


@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = ['code','course','user','is_activated']
