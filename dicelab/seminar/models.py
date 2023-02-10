"""
Modules for DB
"""
from django.db import models

class Seminar(models.Model):
    """
    Seminar Table
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    date = models.CharField(max_length=50, null=True)
    speaker = models.CharField(max_length=50, null=True)
    source = models.CharField(max_length=50, null=True)
    year = models.CharField(max_length=50, null=True)
    area = models.CharField(max_length=50, null=True)
    slide = models.CharField(max_length=100, null=True)
    paper = models.CharField(max_length=100, null=True)

    class Meta:
        """
        Tile 관련 Unique 키 설정
        """
        unique_together = ('title', 'date')

    def __str__(self):
        return self.date + "-" + self.title
