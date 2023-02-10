"""
Modules for Data Query & DB Indexing
"""
import json
from typing import Dict
from json import loads
import urllib3
from django.conf import settings
from celery import shared_task
from .models import Demo

http = urllib3.PoolManager()
DEMO_DATABASE_ID = getattr(
    settings, 'DEMO_DATABASE_ID', 'DEMO_DATABASE_ID')
INTERNAL_INTEGRATION_TOKEN = getattr(
    settings, 'INTERNAL_INTEGRATION_TOKEN', 'INTERNAL_INTEGRATION_TOKEN')
Notion = getattr(settings, 'NOTION_VERSION', 'Notion-version')
headers = {
    'Authorization': f'Bearer {INTERNAL_INTEGRATION_TOKEN}',
    'Notion-Version': Notion,
    "Content-Type": "application/json"
}


@shared_task
def set_data():
    """
    DB Indexing
    """
    data = load_notion_api_demo()['body']
    temp = []
    for d in data:
        c, created = Demo.objects.update_or_create(
            title=d['title'], date=d['date'])
        c.description = d['description']
        c.video = d['video']
        c.save()
        temp.append([d['title'], d['date']])
    # Data Delete
    for db in Demo.objects.all():
        if not [db.title, db.date] in temp:
            Demo.objects.get(title=db.title, date=db.date).delete()


def get_block(id):
    """
    Data Query
    """
    url = f"https://api.notion.com/v1/blocks/{id}/children?page_size=100"
    response = http.request('GET',
                            url,  # json파일로 인코딩
                            headers=headers,
                            retries=False)
    source: Dict = loads(response.data.decode('utf-8'))  # 자료형 명시
    with open("data.json", "w") as f:
        json.dump(source, f)
    for r in source['results']:
        if 'paragraph' in r:
            text = r['paragraph']['text'][0]['plain_text']
            print(text)
            return text
        else:
            return ''


def print_block(data):
    for d in data:
        print(d['block'])
        if 'child' in d:
            print_block(d['child'])


def load_notion_api_demo():
    """
    Data Query
    """
    url = f"https://api.notion.com/v1/databases/{DEMO_DATABASE_ID}/query"
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
            "property": "date",
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
        title = r['properties']['title']['title'][0]['plain_text']
        try:
            page_id = r['id']
            description = get_block(page_id)
        except KeyError:
            description = ''
        try:
            if r['properties']['video']['files']:
                video = r['properties']['video']['files'][0]['name']
            else:
                video=''
        except KeyError:
            video = ''
        try:
            date = r['properties']['date']['date']['start'].replace('/', '.')
        except KeyError:
            date = ''
        data.append({
            'title': title,
            'date': date,
            'description': description,
            'video': video
        })
    return {
        'statusCode': 200,
        'body': data
    }
