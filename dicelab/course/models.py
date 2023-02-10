""" Import Django DB Models """
from django.db import models

class Semester(models.Model):
    """
    하나의 학기들이 가지는 DB Table
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, blank=True)
    year = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.year + " " + self.title


class Course(models.Model):
    """
    하나의 과목들이 가지는 DB Table
    """
    code = models.CharField(max_length=10, default='',blank=True)
    name = models.CharField(max_length=100, blank=False, default='', primary_key=True)
    semester = models.ManyToManyField(
        Semester, related_name='semester')

    def __str__(self):
        return str(self.name)
