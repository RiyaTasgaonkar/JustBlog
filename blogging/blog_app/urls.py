from django.urls import path,include
from django.contrib.auth import views as authViews
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('posts/',views.posts, name='posts'),
    path('register/',views.register,name='register'),
    path('login/',authViews.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',views.logout_view,name='logout'),
]