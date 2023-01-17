from django.db import models
from django.contrib.auth.models import User
class Book(models.Model):
    title=models.CharField(max_length=100,null=False)
    price=models.FloatField(null=False)
    author=models.CharField(max_length=100,null=False)
    publisher=models.CharField(max_length=100,null=False)
class BRMuser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=20,null=False)
    