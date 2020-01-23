from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world")

def home(request):
    return HttpResponse("<h1 style='color:red'>Welcome</h1>")

def check(request,name,age):
    if age>=18:
        return HttpResponse("<h1 style='color:coral'>{} is eligible to vote".format(name))
    else:
        return HttpResponse("<h1 style='color:coral'>{} is not eligible to vote".format(name))
        