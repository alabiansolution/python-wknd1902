from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello world')

def about(request):
    return HttpResponse('About our orgarnization')

def contact(request):
    return HttpResponse('Contact us on FaceBook')

def dashboard(request):
    return HttpResponse('Our Dashboard')

def enquiries(request):
    return HttpResponse('Make enquiries here')
