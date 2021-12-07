from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AdPageForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your Freelance name", "class": "form-control"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Your Freelance name", "class": "form-control"}))
    additional_info = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Additional Information", "class": "form-control"}))
    price = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={"placeholder": "Minimum price is 1", "class": "form-control"}))
    creator = forms.CharField(widget=forms.TextInput(attrs={"type": "hidden"}))