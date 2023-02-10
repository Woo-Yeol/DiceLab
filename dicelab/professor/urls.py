"""
Modules for Professor Page
"""
from django.urls import path
from .views import professor
urlpatterns = [
    path('', professor, name="professor"),
]