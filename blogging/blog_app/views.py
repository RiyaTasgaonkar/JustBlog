from django.shortcuts import render,redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

@login_required
def posts(request): 
    posts=Post.objects.all().order_by('-date')
    user=request.user.username
    return render(request,'posts.html', {'posts':posts,'user':user})

@login_required
def my_posts(request):
    u=request.user.username
    posts=Post.objects.filter(postAuthor__exact=request.user.id).order_by('-date')
    return render(request,'my_posts.html', {'posts':posts,'user':u})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request,'You have been logged out.')
    return redirect('home')

class detail_view(LoginRequiredMixin, DetailView):
    model=Post
    template_name='post-details.html'

class upload(LoginRequiredMixin,CreateView):
    model=Post
    template_name='upload.html'
    fields=['postTitle','postContent']
    def form_valid(self, form):
        form.instance.postAuthor=self.request.user
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('my_posts')

class update(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    template_name='upload.html'
    fields=['postTitle','postContent']
    def form_valid(self, form):
        form.instance.postAuthor=self.request.user
        return super().form_valid(form)

    def test_func(self):
        p=self.get_object()
        return p.postAuthor==self.request.user
    
    def get_success_url(self):
        messages.info(self.request,'Post has been updated.')
        return reverse('my_posts')
 
class delete_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name='delete.html'

    def test_func(self):
        p=self.get_object()
        return p.postAuthor==self.request.user

    def get_success_url(self):
        messages.info(self.request,'Post has been deleted.')
        return reverse('my_posts')