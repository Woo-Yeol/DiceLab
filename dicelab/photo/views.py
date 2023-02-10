"""
Modules for Photo Page
"""
from django.shortcuts import render
from .tasks import set_data
from .models import School,Activity


def photo(request):
    """
    Photo 페이지 렌더링 함수
    """
    
    # set_data()
    school = School.objects.order_by('-title')
    activity = Activity.objects.order_by('-date')
    return render(request, 'photo.html', {'school': school, 'activity': activity})
