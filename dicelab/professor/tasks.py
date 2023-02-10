"""
Modules for Data Query & DB Indexing
"""
from json import loads
from typing import Dict
from celery import shared_task
import urllib3
from django.conf import settings
from .models import Professor


http = urllib3.PoolManager()
Page_ID = getattr(
    settings, 'PAGE_ID', 'Page_ID')
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
    DB Indexing
    """
    for db in Professor.objects.all():
        db.delete()
    data = load_notionAPI_professor()
    target = Professor.objects.get_or_create(
        body=data['body'], image=data['image'])


def load_notionAPI_professor():
    """
    Data Query
    """
    url = f"https://api.notion.com/v1/blocks/{Page_ID}/children?page_size=100"
    response = http.request('GET',
                            url,  # json파일로 인코딩
                            headers=headers,
                            retries=False)
    source: Dict = loads(response.data.decode('utf-8'))  # 자료형 명시
    page = []
    paragraph = {}
    image = 0
    for r in source['results']:
        if 'image' in r:
            image += 1
        elif 'paragraph' in r:
            try:
                line = r['paragraph']['text'][0]['plain_text']
                if len(paragraph):
                    paragraph['text'] = text
                    page.append(paragraph)
                paragraph = {}
                paragraph['title'] = line
                text = []
            except:
                continue
        elif 'bulleted_list_item' in r:
            try:
                line = r['bulleted_list_item']['text']
                line = ''.join([l['plain_text'] for l in line])
                text.append(line)
            except:
                continue
        else:
            continue
    if len(paragraph):
        paragraph['text'] = text
        page.append(paragraph)
    return {
        'statusCode': 200,
        'body': page,
        'image': image
    }
