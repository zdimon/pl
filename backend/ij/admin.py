from django.contrib import admin

# Register your models here.

from ij.models import *

class CityAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(City, CityAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['image_tag','publicname', 'username', 'about', 'email', 'telegram', 'skype', 'is_master']

admin.site.register(UserProfile, UserProfileAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'youdo_id', 'youdo_key']

admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'youdo_id']
    list_filter = ['category']

admin.site.register(SubCategory, SubCategoryAdmin)

class OptionInline(admin.TabularInline):
    list_display = ['value', 'text']
    model = Option


class Control2SubCategoryInine(admin.TabularInline):
    model = Control.subcategory.through
    extra = 3

class ControlAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'type', 'alias']
    list_filter = ['type', 'category']
    inlines = [Control2SubCategoryInine, OptionInline]
        

admin.site.register(Control, ControlAdmin)

class SuggestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'subcategory']

admin.site.register(Suggestion, SuggestionAdmin)


class Order2ControlInline(admin.TabularInline):
    list_display = ['control', 'value']
    model = Order2Control


class OrderAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'category', 'subcategory', 'user']
    inlines = [Order2ControlInline]

admin.site.register(Order, OrderAdmin)

class OfferAdmin(admin.ModelAdmin):
    list_display = ['desc', 'user', 'order']


admin.site.register(Offer, OfferAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['owner', 'contact', 'created_at']


admin.site.register(Contact, ContactAdmin)

class ChatMessageInlineAdmin(admin.TabularInline):
    model = ChatMessage

class ChatRoom2UserInlineAdmin(admin.TabularInline):
    model = ChatRoom2User

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'token', 'search_key']
    inlines = [ChatRoom2UserInlineAdmin, ChatMessageInlineAdmin]

@admin.register(CatFilter)
class CatFilterAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'user', 'subcategory']
    

