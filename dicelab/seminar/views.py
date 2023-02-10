"""
Modules for Seminar Page
"""
from django.shortcuts import render
from .models import Seminar
from .tasks import set_data


def seminar(request):
    """
    Seminar 페이지 랜더링하는 함수
    """
    # set_data()
    seminar = Seminar.objects.order_by('-date')
    return render(request, 'seminar.html', {'seminar': seminar})
