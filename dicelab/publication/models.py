from django.db import models
import datetime


label = [('International_Paper', 'International_Paper'),
         ('Domestic_Paper', 'Domestic_Paper')]


def year_choices():
    return [(str(r), str(r)) for r in range(2000, datetime.date.today().year + 1)]


def current_year():
    return str(datetime.date.today().year)


# DB

class Year(models.Model):
    year = models.CharField(max_length=10,
                            choices=year_choices(), default=current_year())

    def __str__(self):
        return str(self.year)


class Pat_Year(models.Model):
    year = models.CharField(max_length=10,
                            choices=year_choices(), default=current_year())

    def __str__(self):
        return str(self.year)


class Paper(models.Model):
    title = models.CharField(max_length=50,
                             default='', primary_key=True)
    label = models.CharField(
        max_length=20, choices=label, default='International_Paper')
    paper_link = models.CharField(max_length=30, null=True)
    thesis = models.CharField(max_length=20, null=True)
    year = models.ManyToManyField(
        Year, related_name='paper', blank=True)
    assign = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title


class Patents(models.Model):
    title = models.CharField(max_length=50,
                             default='', primary_key=True)
    country = models.CharField(max_length=20, null=True)
    num = models.CharField(max_length=20, null=True)
    year = models.ManyToManyField(
        Pat_Year, related_name='patents', blank=True)
    assign = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title
