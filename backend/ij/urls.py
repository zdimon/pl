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
                    GoogleAuthView, \
                    ProfileEditView, \
                    ContactListView, \
                    ContactDeleteView, \
                    GetRoomView, \
                    GetRoomMessageView, \
                    CreateRoomMessageView, \
                    CheckEmailView

urlpatterns = [ 
   
    path('city/list',CityListView.as_view()),
    path('category/list',CategoryListView.as_view()),
    path('control/list',ControlListView.as_view()),

    path('login',LoginView.as_view()),
    path('suggestion/list',SuggestionListView.as_view()),
    path('order/create',CreateOrderView.as_view(),name="create_order"),
    path('order/list',OrderListView.as_view(),name="order_list"),
    path('offer/create',CreateOfferView.as_view(),name="create_offer"),
    path('offer/my',UserOfferListView.as_view(),name="my_offers"),
    path('offer/order',OrderOfferListView.as_view(),name="order_offers"),

    # registartion
    path('registration',RegistrationView.as_view()),
    path('registration/check/email',CheckEmailView.as_view(),name="check_email"),

    path('google/auth',GoogleAuthView.as_view(),name="google_auth"),
    path('profile/edit/<int:pk>',ProfileEditView.as_view(),name="profile_edit"),
    

    # contact
    path('contact/list',ContactListView.as_view(),name="contact_list"),
    path('contact/delete/<int:pk>',ContactDeleteView.as_view(),name="contact_delete"),
    
    # chat
    path('chat/get_room/<int:user_id>',GetRoomView.as_view(),name="chat_room_get"),
    path('chat/get_room_messages',GetRoomMessageView.as_view(),name="chat_room_messages"),
    path('chat/create_message/',CreateRoomMessageView.as_view(),name="chat_message_create"),

    
    
]
