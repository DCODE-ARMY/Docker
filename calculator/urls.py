
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/add/', views.add_numbers_api, name='add_api'),
]
