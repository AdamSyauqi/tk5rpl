from django.db import models
from django.core.validators import *
from datetime import datetime

# Create your models here.

class AdPage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    additional_info = models.TextField(max_length=200)
    price = models.IntegerField()
    creator = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class rateAndComment(models.Model):
    user=models.CharField(max_length=120)
    ad = models.CharField(max_length=1000000)
    review=models.CharField(max_length=1000000)
    score=(
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )
    rating=models.IntegerField(choices=score,default=3)
    date=models.DateTimeField(default=datetime.now,blank=True)