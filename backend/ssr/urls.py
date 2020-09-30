from django.urls import path, include
from ssr.web.views import web_index
from ssr.mobi.views import mobi_index

urlpatterns = [ 
   
    path('web/',web_index),
    path('mobi/',mobi_index),
    path('mobi/tabs/<slug:slug>',mobi_index),
    path('mobi/tabs/order/<slug:slug>',mobi_index),
]
