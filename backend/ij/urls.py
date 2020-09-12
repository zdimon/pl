from django.urls import path, include
from ij.views import CityListView, \
                    CategoryListView, \
                    ControlListView, \
                    RegistrationView, \
                    LoginView, \
                    SuggestionListView, \
                    CreateOrderView, \
                    OrderListView

urlpatterns = [ 
   
    path('city/list',CityListView.as_view()),
    path('category/list',CategoryListView.as_view()),
    path('control/list',ControlListView.as_view()),
    path('registration',RegistrationView.as_view()),
    path('login',LoginView.as_view()),
    path('suggestion/list',SuggestionListView.as_view()),
    path('order/create',CreateOrderView.as_view(),name="create_order"),
    path('order/list',OrderListView.as_view(),name="order_list"),
]
