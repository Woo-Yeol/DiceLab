""" Import for Url functions """
from django.urls import path
from .views import course

urlpatterns = [
    path('', course, name="course"),
]
