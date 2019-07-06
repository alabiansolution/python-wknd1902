from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'themes/index.html', {'home_key' : 'Welcome to my website'})

def about(request):
     args = {
            'title': 'About Us',
            'content' : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci,',
       }
     return render(request, 'themes/about.html', context=args)

def service(request):
    return render(request, 'themes/service.html', {'service_key' : 'Our Service'})

def contact(request):
    return render(request, 'themes/contact.html', {'contact_key' : 'Contact Us Page'})
