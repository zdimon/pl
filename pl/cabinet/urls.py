from django.urls import path, include
from cabinet.views import index, edit_profile, payments

urlpatterns = [ 
    path('',index, name="cabinet_index"),
    path('profile/edit',edit_profile, name="edit_profile"),
    path('payments',payments, name="payments"),
]