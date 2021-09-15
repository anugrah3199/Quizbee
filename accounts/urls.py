from django.urls import path,include
from django.contrib import admin
from accounts.views import register
from . import urls

urlpatterns = [
    
    path('register',register, name = 'register'),
]