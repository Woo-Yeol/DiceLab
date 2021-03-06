# Generated by Django 3.2.6 on 2022-01-29 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=50, null=True)),
                ('speaker', models.CharField(max_length=50, null=True)),
                ('source', models.CharField(max_length=50, null=True)),
                ('year', models.CharField(max_length=50, null=True)),
                ('area', models.CharField(max_length=50, null=True)),
                ('slide', models.CharField(max_length=50, null=True)),
                ('paper', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
