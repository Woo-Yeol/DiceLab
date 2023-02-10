"""
Modules for Admin Page
"""
from django.contrib import admin
from .models import Paper, Year, Patents, PatentYear

# Register your models here.

admin.site.register(Year)
admin.site.register(PatentYear)
admin.site.register(Paper)
admin.site.register(Patents)
