from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    postTitle=models.CharField(max_length=250)
    postContent=models.TextField(null=False)
    date=models.DateTimeField(default=timezone.now)
    postAuthor=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.postTitle

class Subscription(models.Model):
    Male = 'M'
    Female = 'F'
    RatherNotSay = 'O'
    Daily='D'
    Weekly='W'
    Monthly='MT'
    GENDER_CHOICES = ((Male, 'Male'),(Female, 'Female'),(RatherNotSay,'Rather Not Say'),)
    FREQUENCY_CHOICES = ((Daily, 'Daily'),(Weekly, 'Weekly'),(Monthly,'Monthly'),)

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField(max_length = 254) 
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length = 20, choices = GENDER_CHOICES,default = Male)
    frequency=models.CharField(max_length = 20, choices = FREQUENCY_CHOICES,default = Daily)

    def __str__(self):
        return self.email



