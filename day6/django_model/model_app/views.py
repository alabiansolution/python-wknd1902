from django.shortcuts import render
from model_app.models import Category, ContactModel, Post
from django.contrib.auth.models import User


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
