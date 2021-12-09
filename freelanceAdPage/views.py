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
    #unsorted_reviews = rateAndComment.objects.all().filter(target=freelancer).filter(title=ad)
    #review=sorted(list(unsorted_reviews.values()),key=lambda k:k['date'])[0]
    #return render(request, 'freelance_ad_page.html',{'review':review})
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

def review(request,freelancer,ad):
    if request.method == 'POST':
        target = request.POST.get('target')
        user = request.user.username
        review = request.POST.get('review')
        rating = request.POST.get('rating')
        title = request.POST.get('title')
        if rateAndComment.objects.filter(user=user).filter(target=target).exists():
            old = rateAndComment.objects.all().filter(title=title).filter(user=user).filter(target=target)
            old.delete()
        new = rateAndComment.objects.create(user=user,target=target,title=title,review=review,rating=rating)
        new.save()
    unsorted_reviews = rateAndComment.objects.all().filter(target=freelancer).filter(title=ad)
    reviews=sorted(list(unsorted_reviews.values()),key=lambda k:k['date'])
    return render(request, 'review.html',{'reviews':reviews,'friend':freelancer,'ad':ad})