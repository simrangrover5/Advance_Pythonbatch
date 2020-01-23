from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("home/",views.home),
    path('login/',views.login),
    path('afterlogin/',views.afterlogin),
    path('signup/',views.signup),
    path('aftersignup/',views.aftersignup),
    path('forgot/',views.forgot),
    path('logout/',views.logout)
]