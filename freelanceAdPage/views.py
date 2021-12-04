from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def browse_page(request):
    return render(request, 'browse_page.html')

def browse_fail(request):
    return render(request, 'browse_fail.html')

def freelance_ad_page(request):
    return render(request, 'freelance_ad_page.html')

def create_ad_page(request):
    print(AdPage.objects.all())
    form = AdPageForm()
    if request.method == "POST":
        form = AdPageForm(request.POST)
        if form.is_valid():
            AdPage.objects.create(**form.cleaned_data)
            form = AdPageForm()
    context = {
        'form' : form
    }
    return render(request, 'create_ad_page.html', context)