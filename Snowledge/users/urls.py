  
from django.urls import path
from . import views as users_views
from django.contrib.auth import views as auth_views
from .forms import *

urlpatterns = [
    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]