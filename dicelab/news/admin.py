"""
Modules for Admin Page
"""
from django.contrib import admin
from .models import News
# Register your models here.

admin.site.register(News)