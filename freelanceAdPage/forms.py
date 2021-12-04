from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AdPageForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    additional_info = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()