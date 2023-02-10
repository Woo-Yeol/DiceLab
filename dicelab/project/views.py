"""
Modules for Project Page
"""
from django.shortcuts import render
from .tasks import set_data
from .models import AiChallenge, Project


def project(request):
    """
    Project 페이지 랜더링하는 함수
    """
    # set_data()
    projects = Project.objects.order_by('-status', '-date')
    ai_challenges = AiChallenge.objects.order_by('-date')
    return render(request, 'project.html', {'projects': projects, 'ai_challenges': ai_challenges})
