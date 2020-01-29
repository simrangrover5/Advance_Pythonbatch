from django.urls import path
from . import views

urlpatterns  = [
    path('addblog/',views.addblog),
    path('blogadd/',views.Blogs.as_view()),
    path('myblogs/',views.myblogs),
    path('api/',views.showapi.as_view()),
]