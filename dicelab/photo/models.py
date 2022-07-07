from django.db import models


class Lecture(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name


class School(models.Model):
    title = models.CharField(primary_key=True, max_length=50,)
    lecture = models.ManyToManyField(Lecture)

    def __str__(self):
        return self.title


class Activity(models.Model):
    title = models.CharField(primary_key=True, max_length=100,)
    description = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = (('title', 'date'))

    def __str__(self):
        return self.title
