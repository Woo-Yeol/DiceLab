from celery import shared_task
from django.conf import settings
import urllib3
from typing import Dict
import json
from json import loads
from .models import Research_interests, Linked, Graduated, Alumni, Team

http = urllib3.PoolManager()
Member_Graduate_Database_ID = getattr(
    settings, 'MEMBER_GRADUATE_DATABASE_ID', 'member_graduate_database_ID')
Member_Ungraduate_Database_ID = getattr(
    settings, 'MEMBER_UNGRADUATE_DATABASE_ID', 'member_ungraduate_database_ID')
Member_Urp_Database_ID = getattr(
    settings, 'MEMBER_URP_DATABASE_ID', 'member_urp_database_ID')
Member_Alumni_Database_ID = getattr(
    settings, 'MEMBER_ALUMNI_DATABASE_ID', 'member_alumni_database_ID')
Notion = getattr(settings, 'NOTION_VERSION', 'Notion-version')
Internal_Integration_Token = getattr(
    settings, 'INTERNAL_INTEGRATION_TOKEN', 'Internal_Integration_Token')

headers = {
    'Authorization': f'Bearer {Internal_Integration_Token}',
    'Notion-Version': Notion,
    "Content-Type": "application/json"
}


@shared_task
def set_data():
    data = load_notionAPI_member_graduate()['body']
    # Data Create or Update
    temp = []
    for d in data:
        g, created = Graduated.objects.update_or_create(
            name=d['name'])
        g.course = d['course']
        if d['admission_date'] != None:
            g.admission_date = d['admission_date']
        if d['email'] != None:
            g.email = d['email']
        if d['pic'] != None:
            g.pic = d['pic']
        for r in d['research_interests']:
            obj, created = Research_interests.objects.get_or_create(title=r)
            g.research_interests.add(obj)
            g.save()
        if d['linked'] != None:
            for key, value in d['linked'].items():
                obj, created = Linked.objects.get_or_create(
                    title=key.replace(" : ", ""), link=value)
                g.linked.add(obj)
                g.save()
        temp.append(d['name'])
    data = load_notionAPI_member_alumni()['body']
    for d in data:
        a, created = Alumni.objects.update_or_create(
            name=d['name'])
        a.graduate_year = d['graduate_year']
        if d['course'] != None:
            a.course = d['course']
        else:
            a.course = ''
        obj, created = Team.objects.get_or_create(title=d['team'])
        a.team.add(obj)
        a.save()
        temp.append(d['name'])
    # Data Delete
    for db in Graduated.objects.all():
        if not db.name in temp:
            Graduated.objects.get(name=db.name).delete()
    for db in Alumni.objects.all():
        if not db.name in temp:
            Alumni.objects.get(name=db.name).delete()


def load_notionAPI_member_graduate():
    url = f"https://api.notion.com/v1/databases/{Member_Graduate_Database_ID}/query"
    filter = {  # 가져올 데이터 필터
        "or": [
            {
                "property": "course",
                "select": {
                    "is_not_empty": True
                }
            }
        ]
    }
    sorts = [  # 정렬
        {
            "property": "admission_date",
            "direction": "ascending"
        },
        {
            "property": "name",
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
        try:
            name = r['properties']['name']['title'][0]['plain_text']
        except:
            continue
        course = r['properties']['course']['select']['name']
        try:
            admission_date = r['properties']['admission_date']['select']['name']
        except:
            admission_date = None
        research_interests = [l['name']
                              for l in r['properties']['research_interests']['multi_select']]
        try:
            email = r['properties']['email']['email'].replace("@", "'at'")
        except:
            email = None
        links = ''
        try:
            temp = r['properties']['linked']['rich_text']
            for t in temp:
                links += t['plain_text']
            links = links.split("\n")
            link_title = []
            link_content = []
            for link in links:
                if " : " in link:
                    link_title.append(link)
                else:
                    link_content.append(link)
            linked = dict(zip(link_title, link_content))
        except:
            linked = None
        try:
            pic = r['properties']['pic']['files'][0]['name']
        except:
            pic = None

        data.append({
            'name': name,
            'course': course,
            'admission_date': admission_date,
            'research_interests': research_interests,
            'email': email,
            'linked': linked,
            'pic': pic
        })
    return {
        'statusCode': 200,
        'body': data
    }


def load_notionAPI_member_alumni():
    url = f"https://api.notion.com/v1/databases/{Member_Urp_Database_ID}/query"
    filter = {  # 가져올 데이터 필터
        "or": [
                {
                    "property": "team",
                    "select": {
                        "is_not_empty": True
                    }
                }
        ]
    }
    sorts = [  # 정렬
        {
            "property": "course",
            "direction": "ascending"
        },
        {
            "property": "team",
            "direction": "ascending"
        },
        {
            "property": "name",
            "direction": "ascending"
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
        try:
            name = r['properties']['name']['title'][0]['plain_text']
        except:
            continue
        try:
            course = r['properties']['course']['select']['name']
        except:
            course = None
        team = r['properties']['team']['select']['name']
        graduate_year = r['properties']['graduate_year']['select']['name']
        data.append({
            'name': name,
            'course': course,
            'team': team,
            'graduate_year': graduate_year
        })
    return {
        'statusCode': 200,
        'body': data
    }
