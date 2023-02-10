"""
Modules for News Page
"""
import json
from django.shortcuts import render
from .tasks import set_data
from .models import News


def news(request):
    """
    News Page 렌더링 함수
    """
    # set_data()
    news = News.objects.all().order_by('-date')
    news_list = []
    for n in news:
        temp = {}
        temp['title'] = n.title
        temp['date'] = n.date
        temp['content'] = json.decoder.JSONDecoder().decode(n.content)
        temp['pic'] = n.pic
        temp['column_type'] = n.column_type
        news_list.append(temp)
    return render(request, 'news.html', {'news': news_list})
