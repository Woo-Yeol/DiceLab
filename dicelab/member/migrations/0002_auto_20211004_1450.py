# Generated by Django 3.2.6 on 2021-10-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='graduated',
            name='name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='linked',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='research_interests',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
