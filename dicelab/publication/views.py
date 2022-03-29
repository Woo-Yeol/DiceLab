from django.shortcuts import render
from .tasks import set_data
from .models import Patents, Pat_Year, Paper, Year


def publication(request):
    # set_data()

    paper_year = Year.objects.all().order_by('-year')
    patent_year = Pat_Year.objects.all().order_by('-year')

    paper = Paper.objects.all().order_by('-year', '-label')
    patents = Patents.objects.order_by('-year')

    return render(request, 'publication.html', {'paper_year': paper_year, 'patent_year': patent_year, 'paper': paper, 'patents': patents})
