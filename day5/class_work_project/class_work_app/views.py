from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World!!')

def about(request):
    return HttpResponse('About Us Page')

def contact(request):
    return HttpResponse('Contact Us Page')
