"""
Modules for Project Page
"""
from django.urls import path
from .views import project
urlpatterns = [
    path('', project, name="project"),
]
