from django.urls import path, include
from cabinet.views import index, edit_profile, payments

from cabinet.views import PromocodeList, promo_gen, promo_activate

urlpatterns = [ 
    path('',index, name="cabinet_index"),
    path('profile/edit',edit_profile, name="edit_profile"),
    path('payments',payments, name="payments"),
    path('promo', PromocodeList.as_view(), name="promo"),
    path('promo_gen',promo_gen, name="promo_gen"),
    path('promo_activate/<slug:slug>',promo_activate, name="promo_activate"),
]