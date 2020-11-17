from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.

def home(request):
    return render(request,'index.html')

def register(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully!')
            return redirect('login')
        else:
            messages.info(request,'Account creation be failed :(')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})

def posts(request): 
    posts=Post.objects.all()
    return render(request,'posts.html', {'posts':posts})

def logout_view(request):
    logout(request)
    messages.info(request,'You have been logged out.')
    return redirect('home')
