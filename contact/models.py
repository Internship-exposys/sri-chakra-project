from django.db import models
from phonenumber_field.formfields import PhoneNumberField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True)
    message = models.TextField(unique=True)
