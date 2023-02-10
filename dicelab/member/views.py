"""
Modules for Member Page
"""
from datetime import datetime
from django.shortcuts import render
from django.db.models import Case, When
from .tasks import set_data
from .models import Graduated, Project, Master, Alumni


def member(request):
    """
    Member 페이지 랜더링하는 함수
    """
    # set_data()

    # 년도 선언
    current_year = datetime.now().year + 2
    year = [current_year-x for x in range(current_year - 2020 + 1)]
    course_list = ['Ph.D. Course', 'M.S.-Ph.D. Course',
                   'B.S.-M.S. Course', 'M.S. Course']
    project = {}

    # Order
    preserved = Case(*[When(course=course, then=pos)
                     for pos, course in enumerate(course_list)])

    # Query
    graduated = Graduated.objects.all().order_by(
        preserved, 'admission_date', 'name')
    project_4th = Project.objects.filter(year=year[1])
    project_3rd = Project.objects.filter(year=year[0])
    for y in year:
        if not ((y == year[0]) or (y == year[1])):
            project[y] = Project.objects.filter(year=y)
    master = Master.objects.all().order_by('graduate_year', '-name')
    no_project_alumni = Alumni.objects.filter(
        project=None, graduate_year=2020, course='Alumni').order_by('graduate_year')

    return render(request, 'member.html', {'graduated': graduated, 'project_4th': project_4th, 'project_3rd': project_3rd, 'project': project, 'master': master, 'no_project_alumni': no_project_alumni})
