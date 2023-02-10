"""
Modules for Admin Page
"""
from django.contrib import admin
from .models import School, Lecture, Activity
# Register your models here.

admin.site.register(School)
admin.site.register(Lecture)
admin.site.register(Activity)
