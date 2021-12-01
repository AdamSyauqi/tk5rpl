from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
#from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def browse_page(request):
    return render(request, 'browse_page.html')