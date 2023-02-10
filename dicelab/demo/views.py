"""
Modules for Demo Page
"""
from django.shortcuts import render
from .models import Demo
from .tasks import set_data

# Create your views here.


def demo(request):
    """
    Demo 페이지 렌더링 함수
    """
    # set_data()
    demo = Demo.objects.exclude(date__exact='').exclude(video__exact='').order_by('-date')
    print(demo)
    demo_list = []
    for n in demo:
        temp = {}
        temp['title'] = n.title
        temp['date'] = n.date
        temp['description'] = n.description
        temp['video'] = n.video
        demo_list.append(temp)
    return render(request, 'demo.html', {'demo': demo_list})
