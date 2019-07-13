from django.shortcuts import render
from model_app.models import Category, ContactModel, Post
from django.contrib.auth.models import User
from model_app.forms import BasicForm, MoreForm, ConsoleFile, ContactForm

# Create your views here.

def index(request):
    post = Post.objects.order_by('-created_at')
    return render(request, 'themes/index.html', {'mypost':post})

def detail(request, post_id):
    post_detail = Post.objects.get(pk=post_id)
    return render(request, 'themes/detail.html', {'detail':post_detail})

def users(request):
    user_list = User.objects.all()
    return render(request, 'themes/user.html', {'users':user_list})

def basic_form(request):
    basic = BasicForm()
    return render(request, 'themes/basic.html', {'my_basic':basic})

def form_page(request):
    form1 = MoreForm()
    if request.method == 'POST':
        form2 = ConsoleFile(request.POST)
        if form2.is_valid():
            name = form2.cleaned_data['name']
            email = form2.cleaned_data['email']
            message = form2.cleaned_data['message']
            print(name+'\n'+email+'\n'+message)
    else:
        form2 = ConsoleFile()

    if request.method == 'POST':
        form3 = ContactForm(request.POST)
        if form3.is_valid():
            name = form3.cleaned_data['name']
            email = form3.cleaned_data['email']
            message = form3.cleaned_data['message']
            form3.save(commit=True)
        else:
            form3 = ContactForm()

    args = {
        'my_form1' : form1,
        'my_form2' : form2,
        'my_form3' : form3
    }

    return render(request, 'themes/forms.html', context=args)
