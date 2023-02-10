"""
Import Modules for Rendering Main Page & Data Indexing
"""
import json

from django.shortcuts import render
from course import tasks as ct
from demo import tasks as dt
from member import tasks as mt
from news import tasks as nt
from news.models import News
from project import tasks as prjt
from professor import tasks as prt
from publication import tasks as put
from photo import tasks as ptt
from seminar import tasks as smt


# Create your views here.

def main(request):
    """
    Render Main Page
    """
    raw_news = News.objects.all().order_by('-date')[:5]
    recent_news = []
    for news in raw_news:
        temp = {}
        temp['title'] = news.title
        temp['date'] = news.date
        temp['content'] = json.decoder.JSONDecoder().decode(news.content)
        temp['pic'] = news.pic
        temp['column_type'] = news.column_type
        recent_news.append(temp)
    #set_all_data()
    return render(request, 'main.html', {'recent_news' : recent_news})


def set_all_data():
    """
    DB 날렸을 때 한 번에 모든 데이터 복구시키기 위한 함수
    """
    # All Data
    ct.set_data()
    dt.set_data()
    mt.set_data()
    nt.set_data()
    prjt.set_data()
    prt.set_data()
    put.set_data()
    ptt.set_data()
    smt.set_data()
    print('set_all_data')
