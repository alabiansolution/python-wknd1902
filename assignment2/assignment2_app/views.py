from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,  'themes/index.html', {'home_key' : 'Welcome to my website'})
def about(request):
    return render(request,  'themes/about.html', {'about_key' : 'About Us'})
def services(request):
    return render(request,  'themes/services.html', {'services_key' : 'Our Services'})
def contact(request):
    return render(request,  'themes/contact.html', {'contact_key' : 'KIndly contact Us here'})
