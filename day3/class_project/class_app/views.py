from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello world')

def about(request):
    return HttpResponse('About our organisation')

def contact(request):
    return HttpResponse('You can contact us')

def dashboard(request):
    return HttpResponse('Our Dashboard')

def add_post(request):
    return HttpResponse('You can add post here')

def del_post(request):
    return HttpResponse('You can delete post here')
