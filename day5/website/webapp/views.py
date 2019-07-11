from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<em> Welcome to My Assignment </em>')
def contact(request):
    return HttpResponse('Contact our Organization Here')
def about(request):
    return HttpResponse('About our Organization')
def dashboard(request):
    return HttpResponse('office backend')
def back_office(request):
    return HttpResponse('Back office for Organizational member')
def view_data(request):
    return HttpResponse('view data office for Organizational member')
def add_data(request):
    return HttpResponse('Add data for Organizational member')
