from django.urls import path, include
from cabinet.views import index, edit_profile, payments, show_lesson

from cabinet.views import PromocodeList, promo_gen, promo_activate, faq, access_denite, add_answer

urlpatterns = [ 
    path('',index, name="cabinet_index"),
    path('profile/edit',edit_profile, name="edit_profile"),
    path('payments',payments, name="payments"),
    path('promo', PromocodeList.as_view(), name="promo"),
    path('promo_gen',promo_gen, name="promo_gen"),
    path('promo_activate/<slug:slug>',promo_activate, name="promo_activate"),

    path('access_denite',access_denite, name="access_denite"),

    path('faq',faq, name="faq"),
    path('add_answer/<int:id>',add_answer, name="add_answer"),

    path('lesson_swow/<int:id>',show_lesson, name="show_lesson"),



]