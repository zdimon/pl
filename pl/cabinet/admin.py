from django.contrib import admin

from .models import UserProfile, Promocode, ReplCredit

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'account']
    list_editable = ['account']


@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = ['code','course','user','is_activated']


@admin.register(ReplCredit)
class ReplCreditAdmin(admin.ModelAdmin):
    list_display = ['user','ammount','is_paid']
    list_filter = ['is_paid']