from django.shortcuts import render, redirect
from django.http import HttpResponse

def favelist(request):
    return render(request, 'favelist.html')
