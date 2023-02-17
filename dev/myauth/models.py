from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_midlevel = models.BooleanField(default=False)
    is_lowlevel = models.BooleanField(default=False)
    is_highlevel = models.BooleanField(default=False)
    def __str__(self):
        return self.username


class Mid_level_User(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.first_name)



class Low_level_User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.first_name)


class High_level_User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.first_name)