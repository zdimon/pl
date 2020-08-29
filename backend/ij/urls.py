from django.urls import path, include
from ij.views import CityListView

urlpatterns = [ 
   
    path('city/list',CityListView.as_view()),
]
