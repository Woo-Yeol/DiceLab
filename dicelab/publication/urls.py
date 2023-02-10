"""
Modules for Publication Page
"""
from django.urls import path
from .views import publication
urlpatterns = [
    path('', publication, name="publication"),
]
