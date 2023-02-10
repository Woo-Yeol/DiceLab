"""
Modules for DB
"""
from django.db import models


class ResearchInterests(models.Model):
    """
    관심연구분야 테이블
    """
    title = models.CharField(max_length=20)

    def __str__(self):
        return str(self.title)


class Linked(models.Model):
    """
    연락처 링크 테이블
    """
    title = models.CharField(max_length=20)
    link = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return str(self.title)


class Graduated(models.Model):
    """
    대학원생 테이블
    """
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=30, blank=True)
    admission_date = models.CharField(max_length=10, blank=True)
    research_interests = models.ManyToManyField(
        ResearchInterests, related_name='graduated', blank=True)
    email = models.CharField(max_length=30, blank=True)
    pic = models.CharField(max_length=20, blank=True)
    linked = models.ManyToManyField(
        Linked, related_name='graduated', blank=True)

    def __str__(self):
        return str(self.name)


class Team(models.Model):
    """
    졸업작품 팀 테이블
    """
    title = models.CharField(max_length=20)

    def __str__(self):
        return str(self.title)


class Project(models.Model):
    """
    졸업작품 테이블
    """
    title = models.CharField(max_length=40)
    year = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.title)


class Thesis(models.Model):
    """
    대학원 석사 졸업 논문 테이블
    """
    title = models.CharField(max_length=20)
    paper_link = models.CharField(max_length=50, blank=True, null=True)
    slide_link = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.title)


class Master(models.Model):
    """
    대학원 석사 테이블
    """
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=30, blank=True)
    graduate_year = models.CharField(max_length=10, blank=True)
    thesis = models.ManyToManyField(
        Thesis, related_name='master', blank=True)
    email = models.CharField(max_length=30, blank=True)
    pic = models.CharField(max_length=20, blank=True)
    linked = models.ManyToManyField(
        Linked, related_name='master', blank=True)
    employment = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.name)


class Alumni(models.Model):
    """
    졸업생 테이블
    """
    name = models.CharField(max_length=10)
    course = models.CharField(max_length=30, blank=True)
    team = models.ManyToManyField(Team, related_name='alumni')
    graduate_year = models.CharField(max_length=10, null=True)
    project = models.ManyToManyField(
        Project, related_name='alumni', blank=True)

    def __str__(self):
        return str(self.name)
