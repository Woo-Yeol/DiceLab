"""
Modules for DB
"""
import datetime
from django.db import models


label = [('International_Paper', 'International_Paper'),
         ('Domestic_Paper', 'Domestic_Paper')]


def year_choices():
    """
    2000년부터 오늘까지 연도 튜블의 리스트 반환
    """
    return [(str(r), str(r)) for r in range(2000, datetime.date.today().year + 1)]


def current_year():
    """
    올해년도 반환 함수
    """
    return str(datetime.date.today().year)

# DB
class Year(models.Model):
    """
    Year 테이블
    """
    year = models.CharField(max_length=10,
                            choices=year_choices(), default=current_year())

    def __str__(self):
        return str(self.year)


class PatentYear(models.Model):
    """
    Patent Year Table
    """
    year = models.CharField(max_length=10,
                            choices=year_choices(), default=current_year())

    def __str__(self):
        return str(self.year)


class Paper(models.Model):
    """
    Paper(논문) Table
    """
    title = models.CharField(max_length=100,
                             default='', primary_key=True)
    label = models.CharField(
        max_length=20, choices=label, default='International_Paper')
    paper_link = models.CharField(max_length=100, null=True)
    thesis = models.CharField(max_length=100, null=True)
    year = models.ManyToManyField(
        Year, related_name='paper', blank=True)
    assign = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.title)


class Patents(models.Model):
    """
    Patent(특허) Table
    """
    title = models.CharField(max_length=100,
                             default='', primary_key=True)
    country = models.CharField(max_length=100, null=True)
    num = models.CharField(max_length=100, null=True)
    year = models.ManyToManyField(
        PatentYear, related_name='patents', blank=True)
    assign = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.title)
