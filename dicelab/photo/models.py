"""
Modules for DB
"""
from django.db import models


class Lecture(models.Model):
    """
    School에서 진행하는 강의 테이블
    """
    name = models.CharField(primary_key=True, max_length=50)
    url = models.URLField()

    def __str__(self):
        return str(self.name)


class School(models.Model):
    """
    계절별 다이스 스쿨 테이블
    """
    title = models.CharField(primary_key=True, max_length=50,)
    lecture = models.ManyToManyField(Lecture)

    def __str__(self):
        return str(self.title)


class Activity(models.Model):
    """
    외부 활동 및 학회 참석 등의 활동 테이블
    """
    title = models.CharField(primary_key=True, max_length=100,)
    description = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        """
        메타 데이터
        """
        unique_together = (('title', 'date'))

    def __str__(self):
        return str(self.title)
