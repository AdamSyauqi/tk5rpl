from django import forms
from .models import Anggota
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
	class Meta:
		model = Anggota
		fields = ['username','email','password1','password2','role']
		widgets = {
		'username': forms.TextInput(attrs={'class':'input','placeholder':'Username...'}),
		'email': forms.TextInput(attrs={'class':'input','placeholder':'Email...'}),
		'role': forms.Select(choices=((1,'Freelancer'),(2,'Employer')))
		}

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password...'})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Retype password...'})