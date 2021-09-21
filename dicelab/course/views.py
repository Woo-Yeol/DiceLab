from django.shortcuts import render
from .tasks import *
from django.core.cache import cache
from .models import *

from .forms import *

# Create your views here.
load_init_data = False


# def course(request):
#     global load_init_data
#     if load_init_data:
#         semester = cache.get('semester')
#         set_cache.delay()
#     else:
#         load_init_data = True
#         semester = cache.set(
#             'semester', load_notionAPI_course()['body'])
#         semester = cache.get('semester')
#     return render(request, 'course.html', {'semester': semester})

def course(request):
    set_data()
    courses = Course.objects.all()
    form = CoursesCreationForm()
    if request.method == "POST":
        print(request.POST)
    return render(request, 'course.html', {'form': form, 'course': course})
