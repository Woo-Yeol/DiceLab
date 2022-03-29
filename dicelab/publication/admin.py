from django.contrib import admin
from .models import Paper, Year, Patents, Pat_Year

# Register your models here.

admin.site.register(Year)
admin.site.register(Pat_Year)
admin.site.register(Paper)
admin.site.register(Patents)
