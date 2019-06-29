from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<em>My Second App</em>')

# Create your views here.
def about(request):
    return HttpResponse('About our organization')
