"""
Modules for DB

"""
from django.db import models

# Create your models here.


class Project(models.Model):
    """
    Project 테이블
    """
    title = models.CharField(max_length=20, null=False,
                             default='', primary_key=True)
    date = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    assign = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    label = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)


class AiChallenge(models.Model):
    """
    AI Challenge 테이블
    """
    title = models.CharField(max_length=20, null=False,
                             default='', primary_key=True)
    date = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=20, null=True)
    assign = models.CharField(max_length=50, null=True)
    area = models.CharField(max_length=200, null=True)
    label = models.CharField(max_length=50, null=True)
    award = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.title)
