from django.shortcuts import render
from .tasks import set_data
from .models import Patents, International_Paper, Domestic_Paper, Dom_Year, Pat_Year, Int_Year


def publication(request):
    # set_data()

    international_year = Int_Year.objects.all().order_by('-year')
    patent_year = Pat_Year.objects.all().order_by('-year')
    domestic_year = Dom_Year.objects.all().order_by('-year')

    international_paper = International_Paper.objects.order_by('-year')
    patents = Patents.objects.order_by('-year')
    domestic_paper = Domestic_Paper.objects.order_by('-year')

    return render(request, 'publication.html', {'domestic_year': domestic_year, 'international_year': international_year, 'patent_year': patent_year, 'international_paper': international_paper, 'domestic_paper': domestic_paper, 'patents': patents})
