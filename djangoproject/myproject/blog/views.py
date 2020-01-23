from django.shortcuts import render
from .forms import Blogform
# Create your views here.

def addblog(request):
    f = Blogform()
    return render(request,'blog/blogform.html',{'f':f})
