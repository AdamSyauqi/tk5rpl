from django.db import models
from datetime import datetime

class ISODateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''

class Room(models.Model):
    user=models.CharField(max_length=120)
    target=models.CharField(max_length=120)
    date=ISODateTimeField(default=datetime.now,blank=True)
    last_message=models.CharField(max_length=1000000)

class Message(models.Model):
    sender=models.CharField(max_length=120)
    receiver=models.CharField(max_length=120)
    message=models.CharField(max_length=1000000)
    date=ISODateTimeField(default=datetime.now,blank=True)
    rooms=models.ManyToManyField(Room)