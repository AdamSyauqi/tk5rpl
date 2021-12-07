from django.db import models
from django.core.validators import *

# Create your models here.

class AdPage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    additional_info = models.TextField(max_length=200)
    price = models.IntegerField()
    creator = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
