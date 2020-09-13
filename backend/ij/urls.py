from django.urls import path, include
from ij.views import CityListView, \
                    CategoryListView, \
                    ControlListView, \
                    RegistrationView, \
                    LoginView, \
                    SuggestionListView, \
                    CreateOrderView, \
                    OrderListView, \
                    CreateOfferView, \
                    UserOfferListView, \
                    OrderOfferListView, \
                    GoogleAuthView

urlpatterns = [ 
   
    path('city/list',CityListView.as_view()),
    path('category/list',CategoryListView.as_view()),
    path('control/list',ControlListView.as_view()),
    path('registration',RegistrationView.as_view()),
    path('login',LoginView.as_view()),
    path('suggestion/list',SuggestionListView.as_view()),
    path('order/create',CreateOrderView.as_view(),name="create_order"),
    path('order/list',OrderListView.as_view(),name="order_list"),
    path('offer/create',CreateOfferView.as_view(),name="create_offer"),
    path('offer/my',UserOfferListView.as_view(),name="my_offers"),
    path('offer/order',OrderOfferListView.as_view(),name="order_offers"),

    path('google/auth',GoogleAuthView.as_view(),name="google_auth"),

]
