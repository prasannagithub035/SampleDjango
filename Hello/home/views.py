from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("This is your index page")

def services(request):
    return HttpResponse("This is your services page")

def AboutUs(request):
    return HttpResponse("This is your aboutUs page")

def contact(request):
    return HttpResponse("This is your contact page")

