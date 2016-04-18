from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Contact(models.Model):
    first_name = models.TextField(default='')
    last_name = models.TextField(default='')
    phone_number = models.TextField(default='')
    email = models.TextField(default='')
    message = models.TextField(default='')
