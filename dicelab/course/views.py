""" Import Django views Functions """
from django.shortcuts import render
from .tasks import set_data
from .models import Semester,Course


def course(request):
    """
    Course 페이지 랜더링하는 함수
    """
    # set_data()
    semesters = Semester.objects.order_by('-year','title')
    courses = Course.objects.all()
    return render(request, 'course.html', {'semesters': semesters, 'courses': courses})
