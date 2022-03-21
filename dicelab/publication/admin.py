from django.contrib import admin
from .models import Patents, International_Paper, Domestic_Paper, Dom_Year, Pat_Year, Int_Year

# Register your models here.

admin.site.register(Dom_Year)
admin.site.register(Int_Year)
admin.site.register(Pat_Year)
admin.site.register(International_Paper)
admin.site.register(Domestic_Paper)
admin.site.register(Patents)
