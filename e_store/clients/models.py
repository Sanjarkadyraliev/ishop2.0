from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name= models.CharField(max_length=50)
    date_birth = models.DateField(default=date.today())
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    phone = models.IntegerField(max_length=15)


    def __str__(self):
        return f"{self.full_name}"
