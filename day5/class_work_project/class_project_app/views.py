from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Welcome to Class work project')
def about(request):
    return HttpResponse('About Class work project')
def contact(request):
    return HttpResponse('Contact Me As the Owner of  Class work project')
