from django.shortcuts import render
from .tasks import *
from .models import *


def photo(request):
    set_data()
    school = School.objects.order_by('-title')
    activity = Activity.objects.order_by('-date')
    return render(request, 'photo.html', {'school': school, 'activity': activity})
