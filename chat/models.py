from django.db import models
from datetime import datetime

class Room(models.Model):
    user=models.CharField(max_length=120)
    target=models.CharField(max_length=120)
    date=models.DateTimeField(default=datetime.now,blank=True)
    last_message=models.CharField(max_length=1000000)

class Message(models.Model):
    sender=models.CharField(max_length=120)
    receiver=models.CharField(max_length=120)
    message=models.CharField(max_length=1000000)
    date=models.DateTimeField(default=datetime.now,blank=True)
    rooms=models.ManyToManyField(Room)