from django.urls import path
from . import views

urlpatterns  = [
    path('addblog/',views.addblog),
    path('blogadd/',views.Blogs.as_view()),
    path('myblogs/',views.myblogs)
]