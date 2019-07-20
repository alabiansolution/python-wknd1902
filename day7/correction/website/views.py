from django.shortcuts import render
from website.models import AboutModel, ServiceModel

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html', {'home_key': 'Join Us'})

def about(request):
    about = AboutModel.objects.all()
    return render(request, 'frontend/about.html', {'about_key':about})

def detail(request, about_id):
    my_detail = AboutModel.objects.get(pk=about_id)
    return render(request, 'frontend/detail.html', {'detail_key':my_detail})

def service(request):
    service = ServiceModel.objects.all()
    return render(request, 'frontend/services.html', {'service_key':service})
