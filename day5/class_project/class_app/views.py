from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello world!!')

def about(request):
    return HttpResponse('About Us')

def dashboard(request):
    return HttpResponse('Welcome to Dashboard View')

def add_post(request):
    return HttpResponse('Add Post View')
