from django import forms
from .models import Anggota
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
	password1: forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password...'}))
	password2: forms.CharField(label="Password Confirmation", widget=forms.PasswordInput())
	class Meta:
		model = Anggota
		fields = ['username','email','password1','password2']
		widgets = {
		'username': forms.TextInput(attrs={'class':'input','placeholder':'Username...'}),
		'email': forms.TextInput(attrs={'class':'input','placeholder':'Email...'}),
		}