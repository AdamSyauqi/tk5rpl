from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    print(request.user)
    return render(request, 'home.html')

def signup(request):
    if request.user.is_authenticated:
            return redirect('/')
    else:
        form = SignUpForm()
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid() :
                username = form.cleaned_data.get('username')
                user = form.save()
                print(user)
                messages.success(request, username)
                return redirect('/')
    context = {'form':form}
    return render(request, 'signup.html', context)


def login_view(request):
    if request.user.is_authenticated:
            return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            print(username)
            password = request.POST.get('password')
            print(password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login/')