"""
Modules for Data Query & DB Indexing
"""

import json
from typing import Dict
from json import loads
from datetime import date
import urllib3
from django.conf import settings
from celery import shared_task
from .models import School, Lecture, Activity

http = urllib3.PoolManager()
School_Database_ID = getattr(
    settings, 'SCHOOL_DATABASE_ID', 'School_Database_ID')
Photo_Database_ID = getattr(
    settings, 'PHOTO_DATABASE_ID', 'Photo_Database_ID')
Internal_Integration_Token = getattr(
    settings, 'INTERNAL_INTEGRATION_TOKEN', 'Internal_Integration_Token')
Notion = getattr(settings, 'NOTION_VERSION', 'Notion-version')
headers = {
    'Authorization': f'Bearer {Internal_Integration_Token}',
    'Notion-Version': Notion,
    "Content-Type": "application/json"
}


@shared_task
def set_data():
    """
    DB Indexing 코드
    """
    data = load_notion_api_school()['body']
    activity = load_notion_api_activity()['body']
    # Data Create or Update
    temp_data = []
    temp_activity = []

    # School
    for d in data:
        school, created = School.objects.update_or_create(title=d['title'])
        school.lecture.clear()
        for l, u in d['lecture']:
            lecture, created = Lecture.objects.get_or_create(
                name=l)
            lecture.url = u
            lecture.save()
            school.lecture.add(lecture)
            school.save()
        temp_data.append(d['title'])

    # Activity
    for a in activity:
        act, created = Activity.objects.update_or_create(
            title=a['title'])
        act.date = date(a['date'][0], a['date'][1], a['date'][2])
        act.save()
        temp_activity.append(a['title'])

    # Data Delete
    for db in School.objects.all():
        if not db.title in temp_data:
            School.objects.get(title=db.title).delete()
    for db in Activity.objects.all():
        if not db.title in temp_activity:
            Activity.objects.get(title=db.title).delete()


def load_notion_api_activity():
    """
    Activity Data Query from notion api
    """
    url = f"https://api.notion.com/v1/databases/{Photo_Database_ID}/query"
    filter = {  # 가져올 데이터 필터
        "or": [
            {
                "property": "title",
                "text": {
                    "is_not_empty": True
                }
            }
        ]
    }
    sorts = [  # 정렬
        {
            "property": "title",
            "direction": "descending"
        }
    ]
    body = {
        "filter": filter,
        "sorts": sorts
    }
    response = http.request('POST',
                            url,
                            body=json.dumps(body),  # json파일로 인코딩
                            headers=headers,
                            retries=False)
    source: Dict = loads(response.data.decode('utf-8'))  # 자료형 명시
    data = []
    for r in source['results']:
        title = r['properties']['Title']['title'][0]['plain_text']
        date = list(map(int, r['properties']['Date']
                    ['date']['start'].split('-')))
        data.append({
            'title': title,
            'date': date,
        })
    return {
        'statusCode': 200,
        'body': data
    }


def load_notion_api_school():
    """
    School Data Query from notion api
    """
    url = f"https://api.notion.com/v1/databases/{School_Database_ID}/query"
    filter = {  # 가져올 데이터 필터
        "or": [
            {
                "property": "title",
                "text": {
                    "is_not_empty": True
                }
            }
        ]
    }
    sorts = [  # 정렬
        {
            "property": "title",
            "direction": "descending"
        }
    ]
    body = {
        "filter": filter,
        "sorts": sorts
    }
    response = http.request('POST',
                            url,
                            body=json.dumps(body),  # json파일로 인코딩
                            headers=headers,
                            retries=False)
    source: Dict = loads(response.data.decode('utf-8'))  # 자료형 명시
    data = []
    for r in source['results']:
        title = r['properties']['Title']['title'][0]['plain_text']
        lecture = [l['title'][0]['plain_text']
                   for l in r['properties']['lecture']['rollup']['array']]
        url = [l['url']
               for l in r['properties']['url']['rollup']['array']]
        lecture = zip(lecture, url)
        data.append({
            'title': title,
            'lecture': lecture,
        })
    return {
        'statusCode': 200,
        'body': data
    }
