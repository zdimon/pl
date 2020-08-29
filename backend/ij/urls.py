from django.urls import path, include
from ij.views import CityListView, CategoryListView

urlpatterns = [ 
   
    path('city/list',CityListView.as_view()),
    path('category/list',CategoryListView.as_view()),
]
