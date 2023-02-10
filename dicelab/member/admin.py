"""
Modules for Admin Page
"""
from django.contrib import admin
from .models import Thesis, Master, ResearchInterests, Linked, Graduated, Alumni, Team, Project
# Register your models here.

admin.site.register(ResearchInterests)
admin.site.register(Linked)
admin.site.register(Thesis)
admin.site.register(Graduated)
admin.site.register(Alumni)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Master)
