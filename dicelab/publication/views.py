"""
Modules for Publication Page
"""
from django.shortcuts import render
from .tasks import set_data
from .models import Patents, PatentYear, Paper, Year


def publication(request):
    """
    Publication 페이지 랜더링하는 함수
    """
    # set_data()
    paper_year = Year.objects.all().order_by('-year')
    patent_year = PatentYear.objects.all().order_by('-year')

    paper = Paper.objects.all().order_by('-year', '-label')
    patents = Patents.objects.order_by('-year')

    return render(request, 'publication.html', {'paper_year': paper_year, 'patent_year': patent_year, 'paper': paper, 'patents': patents})
