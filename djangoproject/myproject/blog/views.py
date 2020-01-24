from django.shortcuts import render
from .forms import Blogform
from django.views import View
from .models import Addblog
from users.models import AddUser
from django.http import HttpResponse
# Create your views here.

def addblog(request):
    f = Blogform()
    return render(request,'blog/blogform.html',{'f':f})


class Blogs(View):
    def get(self,request):
        error = "Invalid method"
        f = Blogform()
        return render(request,"blog/blogform.html",{'f':f,'error':error})
    
    def post(self,request):
        f = Blogform(request.POST)
        if f.is_valid():
            data = {
                'author' : AddUser.objects.get(email=request.session.get('email')),
                'title' : f.cleaned_data['title'],
                'blog' : f.cleaned_data['blog']
                }
            newblog = Addblog.objects.create(**data)
            newblog.save()
            return render(request,"blog/blogform.html")

        else:
            error = "Invalid form"
            f = Blogform()
            return render(request,"blog/blogform.html",{'f':f,'error':error})

def myblogs(request):
    data = Addblog.objects.filter(author=AddUser.objects.get(email=request.session.get('email')))
    return HttpResponse(data)