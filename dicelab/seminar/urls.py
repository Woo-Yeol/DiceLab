"""
Modules for Seminar Page
"""
from django.urls import path
from .views import seminar
urlpatterns = [
    path('', seminar, name="seminar"),
]
