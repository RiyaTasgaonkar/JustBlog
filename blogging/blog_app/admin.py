from django.contrib import admin
from .models import Post
from .models import Subscription

# Register your models here.
admin.site.register(Post)
admin.site.register(Subscription)
