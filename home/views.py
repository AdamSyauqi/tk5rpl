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
                form.save()
                user = form.cleaned_data.get('username')
                message.success(user)
                login(request, user)
                return redirect('login/')
    context = {'form':form}
    return render(request, 'signup.html', context)


def login(request):
    if request.user.is_authenticated:
            return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def logout(request):
    logout(request)
    return redirect('login/')