from django.urls import path,include
from django.contrib.auth import views as authViews
from . import views
from .views import detail_view,upload,update,delete_view

urlpatterns = [
    path('',views.home, name='home'),
    path('posts/',views.posts, name='posts'),
    path('myposts/',views.my_posts,name='my_posts'),
    path('post/<int:pk>',detail_view.as_view(),name='post-details'),
    path('upload/',upload.as_view(),name='upload'),
    path('post/<int:pk>/update',update.as_view(),name='update'),
    path('post/<int:pk>/delete',delete_view.as_view(),name='delete'),
    path('register/',views.register,name='register'),
    path('login/',authViews.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',views.logout_view,name='logout'),
]