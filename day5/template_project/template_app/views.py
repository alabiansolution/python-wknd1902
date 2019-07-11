from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,  'themes/index.html', {'home_key' : 'Welcome to my website'})
def about(request):
    args = {
            'title' : 'About Us',
            'content' : 'Lorem ipsum dolor sit amet, consectetur. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum' ,

    }
    return render(request,  'themes/about.html',  context=args)
def contact(request):
    args = {
            'Branch1' : ' Lagos',
            'Branch2' : 'Edo' ,
            'Branch3' : 'Benue' ,
            'Branch4' : 'Calabar' ,

    }
    return render(request,  'themes/contact.html',  context=args)
def services(request):
    return render(request,  'themes/services.html', {'service_key' : 'We are Here to Serve you better'})
