"""
Modules for Photo
"""
from django.urls import path
from .views import photo
urlpatterns = [
    path('', photo, name="photo"),
]
