# Generated by Django 3.2.6 on 2022-01-29 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('lecture', models.ManyToManyField(to='school.Lecture')),
            ],
        ),
    ]
