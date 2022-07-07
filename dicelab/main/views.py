from django.shortcuts import render
from course import tasks as ct
from demo import tasks as dt
from member import tasks as mt
from news import tasks as nt
from project import tasks as prjt
from professor import tasks as prt
from publication import tasks as put
from photo import tasks as ptt
from seminar import tasks as set


# Create your views here.

def main(request):
    # set_all_data()
    return render(request, 'main.html')


def set_all_data():
    # All Data
    ct.set_data()
    dt.set_data()
    mt.set_data()
    nt.set_data()
    prjt.set_data()
    prt.set_data()
    put.set_data()
    ptt.set_data()
    set.set_data()
    print('set_all_data')
