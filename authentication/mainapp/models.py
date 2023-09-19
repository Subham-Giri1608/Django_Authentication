from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    current_city = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    college = models.CharField(max_length=100)