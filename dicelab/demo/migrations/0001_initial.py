# Generated by Django 3.2.6 on 2023-01-17 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500)),
                ('video', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=10)),
            ],
        ),
    ]
