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
    freelances = AdPage.objects.all()
    count = len(freelances)
    if request.method == "POST":
        search_freelance = request.POST.get("search_freelance")
        freelances = AdPage.objects.filter(title__contains=search_freelance)
        count = len(freelances)
    context = {
        "freelances": freelances,
        "count": count
    }
    return render(request, 'browse_page.html', context)

def freelance_ad_page(request, pk):
    ad = AdPage.objects.get(id=pk)
    context = {
        "ad": ad
    }
    return render(request, 'freelance_ad_page.html', context)

def create_ad_page(request):
    form = AdPageForm(initial={'creator': request.user})
    print(request.user)
    if request.method == "POST":
        form = AdPageForm(request.POST)
        if form.is_valid():
            AdPage.objects.create(**form.cleaned_data)
            form = AdPageForm()
    context = {
        'form' : form
    }
    return render(request, 'create_ad_page.html', context)

def created_freelance_ad_page_list(request):
    querySet = AdPage.objects.filter(creator=request.user)
    context = {
        "AdPage": querySet
    }
    return render(request, 'freelance_ad_created_list.html', context)

def update_ad_page(request, pk):
    freelance = AdPage.objects.filter(id=pk).values()[0]
    title = freelance['title']
    form = AdPageForm(initial={'title': freelance['title'], 'description': freelance['description'], 'additional_info': freelance['additional_info'], "price": freelance["price"], "creator": freelance["creator"]})
    if request.method == "POST":
        form = AdPageForm(request.POST)
        if form.is_valid():
            AdPage.objects.filter(id=pk).update(**form.cleaned_data)
            return redirect("/freelanceAdPage/created_freelance_ad_page_list")
    context = {
        "form": form,
        "title": title
    }
    return render(request, 'update_ad_page.html', context)

def delete_ad_page(request, pk):
    freelance = AdPage.objects.get(id=pk)
    if request.method == "POST":
        freelance.delete()
        return redirect("/freelanceAdPage/created_freelance_ad_page_list")
    context = {
        "freelance": freelance,
    }
    return render(request, 'delete_ad_page.html', context)