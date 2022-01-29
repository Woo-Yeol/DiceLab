# Generated by Django 3.2.6 on 2022-01-29 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patents',
            fields=[
                ('title', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=20, null=True)),
                ('num', models.CharField(max_length=20, null=True)),
                ('year', models.CharField(max_length=20, null=True)),
                ('assign', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('title', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=20, null=True)),
                ('paper_link', models.CharField(max_length=30, null=True)),
                ('thesis', models.CharField(max_length=20, null=True)),
                ('year', models.CharField(max_length=20, null=True)),
                ('assign', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
