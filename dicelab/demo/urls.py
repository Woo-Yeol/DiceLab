"""
URl for demo
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', demo, name="demo"),
]
