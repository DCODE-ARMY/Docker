"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path,include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('calculator.urls')),
]
