from django.db import models
from django.contrib.auth.models import AbstractUser

class Anggota(AbstractUser):
	username = models.CharField(max_length=50, unique=True)
	email = models.EmailField()
	password1 = models.CharField(max_length=50)
	password2 = models.CharField(max_length=50)
	ROLES = (
		(1,'Freelancer'),
		(2,'Employer'),
	)
	role = models.IntegerField(choices=ROLES, default=1)