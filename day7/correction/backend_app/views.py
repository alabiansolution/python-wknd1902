from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from backend_app.forms import Registration, EditProfileForm

# Create your views here.

def dashboard(request):
    return render(request, 'backend/index.html', {'dash_key':'Dashboard'})


def create_user(request):

    if request.method == 'POST':
        register = Registration(request.POST)
        if register.is_valid():
            register.save()
            return redirect('/backend/')
    else:
        register = Registration()

    return render(request, 'frontend/register.html', {'reg_key': register})


def view_profile(request):
    return render(request, 'backend/view_profile.html', {'user':request.user})

def edit_profile(request):
    if request.method == 'POST':
        edit = EditProfileForm(request.POST, instance=request.user)
        if edit.is_valid():
            edit.save()
            return redirect('/backend/profile_page/')
    else:
        edit = EditProfileForm(instance=request.user)
    return render(request, 'backend/edit_profile.html', {'edit':edit})
