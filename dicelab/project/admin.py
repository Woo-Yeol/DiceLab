"""
Modules for Admin Page
"""
from django.contrib import admin
from .models import AiChallenge, Project

# Register your models here.
admin.site.register(AiChallenge)
admin.site.register(Project)
