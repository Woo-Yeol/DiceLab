# Generated by Django 3.2.6 on 2021-09-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seminal',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=50, null=True)),
                ('speaker', models.CharField(max_length=50, null=True)),
                ('source', models.CharField(max_length=50, null=True)),
                ('year', models.CharField(max_length=50, null=True)),
                ('area', models.CharField(max_length=50, null=True)),
                ('paper', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]