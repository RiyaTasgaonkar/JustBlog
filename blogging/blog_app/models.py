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



