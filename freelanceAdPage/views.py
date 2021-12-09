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
    unsorted_reviews = rateAndComment.objects.all().filter(ad=pk)
    if len(unsorted_reviews) < 1:
        context = {
        "ad": ad,
        "count": len(unsorted_reviews)
    }
    else:
        review=sorted(list(unsorted_reviews.values()),key=lambda k:k['date'])[0]
        context = {
            "ad": ad,
            "review": review,
            "count": len(unsorted_reviews)
        }
    return render(request, 'freelance_ad_page.html', context)

@login_required
def create_ad_page(request):
    if request.user.role == 1:
        form = AdPageForm(initial={'creator': request.user})
        if request.method == "POST":
            form = AdPageForm(request.POST)
            if form.is_valid():
                AdPage.objects.create(**form.cleaned_data)
                form = AdPageForm()
                return redirect("/freelanceAdPage/created_freelance_ad_page_list")
        context = {
            'form' : form
        }
        return render(request, 'create_ad_page.html', context)
    else:
        return redirect('/')

@login_required
def created_freelance_ad_page_list(request):
    if request.user.role == 1:
        querySet = AdPage.objects.filter(creator=request.user)
        context = {
            "AdPage": querySet
        }
        return render(request, 'freelance_ad_created_list.html', context)
    else:
        return redirect('/')

@login_required
def update_ad_page(request, pk):
    if request.user.role == 1:
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
    else:
        return redirect('/')

@login_required
def delete_ad_page(request, pk):
    if request.user.role == 1:
        freelance = AdPage.objects.get(id=pk)
        if request.method == "POST":
            freelance.delete()
            return redirect("/freelanceAdPage/created_freelance_ad_page_list")
        context = {
            "freelance": freelance,
        }
        return render(request, 'delete_ad_page.html', context)
    else:
        return redirect('/')

@login_required
def review(request,ad):
    if request.method == 'POST':
        user = request.user.username
        review = request.POST.get('review')
        rating = request.POST.get('rating')
        ad = request.POST.get('ad')
        if rateAndComment.objects.filter(user=user).exists():
            old = rateAndComment.objects.all().filter(ad=ad).filter(user=user)
            old.delete()
        new = rateAndComment.objects.create(user=user,ad=ad,review=review,rating=rating)
        new.save()
    unsorted_reviews = rateAndComment.objects.all().filter(ad=ad)
    reviews=sorted(list(unsorted_reviews.values()),key=lambda k:k['date'])
    return render(request, 'review.html',{'reviews':reviews,'ad':ad})
