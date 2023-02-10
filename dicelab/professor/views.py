"""
Modules for Professor Page
"""
from django.shortcuts import render
from .tasks import set_data
from .models import Professor


def professor(request):
    """
    Professor 페이지 랜더링하는 함수
    """
    # set_data()
    data = Professor.objects.all()
    page = eval(data.values('body')[0]['body'])
    return render(request, 'professor.html', {'page': page})
