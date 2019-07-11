from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def em(request):
    return HttpResponse('<em> My Second App </em>')
def about(request):
    return HttpResponse('About Our Organization')
def dashboard(request):
    return HttpResponse('Organization Dashboard')
def add_post(request):
    return HttpResponse('Add post to our Organization')
def del_post(request):
    return HttpResponse('Delete Post from our Organization')
def contact(request):
    return HttpResponse('Kindly Contact Us on +278994467')
