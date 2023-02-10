"""
Modules for News
"""
from django.urls import path
from .views import news

urlpatterns = [
    path('', news, name="news"),
]
