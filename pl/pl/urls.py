"""pl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from index.views import index, about

from index.views import LoginView, LogoutView, delivery, oferta, confident

from course.views import liqpay_process

urlpatterns = [
    path('',index),
    path('course/',include('course.urls')),
    path('about-me.html',about, name='about-link'),

    path('oferta.html',oferta, name='oferta'),
    path('confident.html',confident, name='confident'),
    path('delivery.html',delivery, name='delivery'),

    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('accounts/login/', LoginView.as_view(), name='for_login'),
    path('liqpay/process/', liqpay_process),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)