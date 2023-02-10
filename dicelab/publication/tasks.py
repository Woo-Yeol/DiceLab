"""
Modules for Data Query & DB Indexing
"""
import json
from json import loads
from typing import Dict
from celery import shared_task
from django.conf import settings
import urllib3
from .models import Patents, PatentYear, Paper, Year

# 환경 변수 가져오기
http = urllib3.PoolManager()
Publication_Database_ID = getattr(
    settings, 'PUBLICATION_DATABASE_ID', 'Database_ID')
Patents_Database_ID = getattr(
    settings, 'PATENTS_DATABASE_ID', 'Database_ID')
Internal_Integration_Token = getattr(
    settings, 'INTERNAL_INTEGRATION_TOKEN', 'Internal_Integration_Token')
Notion = getattr(settings, 'NOTION_VERSION', 'Notion-version')


@shared_task
def set_data():
    """
    DB Indexing
    """
    paper_data = load_notionAPI_publication()['body']
    pat_data = load_notionAPI_patents()['body']

    # Data Create or Update
    temp_pub = []
    temp_pat = []
    temp_year = []
    temp_patent_year = []

    for d in paper_data:
        paper, created = Paper.objects.update_or_create(title=d['title'])
        paper.label = d['label']
        paper.paper_link = d['paper_link']
        paper.assign = d['assign']
        paper.thesis = d['thesis']
        if d['year'] != None:
            obj, created = Year.objects.get_or_create(
                year=d['year'])
            paper.year.add(obj)
            temp_year.append(d['year'])
            paper.save()
        else:
            paper.save()
        temp_pub.append(d['title'])

    for d in pat_data:
        pat, created = Patents.objects.update_or_create(
            title=d['title'])
        pat.country = d['country']
        pat.num = d['num']
        pat.assign = d['assign']
        if d['year'] != None:
            obj, created = PatentYear.objects.get_or_create(year=d['year'])
            pat.year.add(obj)
            temp_patent_year.append(d['year'])
            pat.save()
        pat.save()
        temp_pat.append(d['title'])

    # Data Delete
    for db in Year.objects.all():
        if not db.year in temp_year:
            Year.objects.get(title=db.year).delete()
    for db in PatentYear.objects.all():
        if not db.year in temp_patent_year:
            PatentYear.objects.get(title=db.year).delete()

    for db in Paper.objects.all():
        if not db.title in temp_pub:
            Paper.objects.get(title=db.title).delete()
    for db in Patents.objects.all():
        if not db.title in temp_pat:
            Patents.objects.get(title=db.title).delete()


def load_notionAPI_publication():
    """
    Data Query
    """
    url = f"https://api.notion.com/v1/databases/{Publication_Database_ID}/query"
    headers = {
        'Authorization': f'Bearer {Internal_Integration_Token}',
        'Notion-Version': Notion,
        "Content-Type": "application/json"
    }
    filter = {
        "or": [
            {
                "property": "label",
                "select": {
                            "is_not_empty": True
                }
            },
        ]
    }
    sorts = [
        {
            "property": "year",
            "direction": "descending"
        }
    ]
    body = {
        "filter": filter,
        "sorts": sorts
    }
    response = http.request('POST',
                            url,
                            body=json.dumps(body),
                            headers=headers,
                            retries=False)

    source: Dict = loads(response.data.decode('utf-8'))
    data = []
    # 정규화 및 정제 후 json에 담기
    for r in source['results']:
        title = r['properties']['title']['title'][0]['plain_text']
        label = r['properties']['label']['select']['name']
        paper_link = r['properties']['paper link']['url']
        thesis = r['properties']['thesis']['rich_text'][0]['plain_text']
        year = r['properties']['year']['select']['name']
        assign = ', '.join([l['name'] for l in r['properties']['assign']
                            ['multi_select']]) if 'assign' in r['properties'] else 'None'
        data.append({
            'title': title,
            'label': label,
            'paper_link': paper_link,
            'thesis': thesis,
            'year': year,
            'assign': assign,
        })
        # TODO implement
    return {
        'statusCode': 200,
        'body': data
    }


def load_notionAPI_patents():
    """
    Data Query
    """
    url = f"https://api.notion.com/v1/databases/{Patents_Database_ID}/query"
    headers = {
        'Authorization': f'Bearer {Internal_Integration_Token}',
        'Notion-Version': Notion,
        "Content-Type": "application/json"
    }
    filter = {
        "or": [
            {
                "property": "year",
                "select": {
                            "is_not_empty": True
                }
            },
        ]
    }
    sorts = [
        {
            "property": "year",
            "direction": "descending"
        }
    ]
    body = {
        "filter": filter,
        "sorts": sorts
    }
    response = http.request('POST',
                            url,
                            body=json.dumps(body),
                            headers=headers,
                            retries=False)

    source: Dict = loads(response.data.decode('utf-8'))
    data = []
    # 정규화 및 정제 후 json에 담기
    for r in source['results']:
        title = r['properties']['title']['title'][0]['plain_text']
        country = r['properties']['country']['select']['name']
        num = r['properties']['num']['rich_text'][0]['plain_text']
        year = r['properties']['year']['select']['name']
        assign = ', '.join([l['name'] for l in r['properties']['assign']
                            ['multi_select']]) if 'assign' in r['properties'] else 'None'

        data.append({
            'title': title,
            'country': country,
            'num': num,
            'year': year,
            'assign': assign,
        })
        # TODO implement
    return {
        'statusCode': 200,
        'body': data
    }
