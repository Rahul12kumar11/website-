

from django.db import models
from django.forms import CharField, EmailField, IntegerField

# Create your models here.

class Message(models.Model):
    name = CharField(max_length=50)
    phone = IntegerField()
    email = EmailField()
    message = CharField(max_length=100)

    def __str__(self):
        return self.name

