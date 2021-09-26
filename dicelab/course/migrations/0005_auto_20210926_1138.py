# Generated by Django 3.2.6 on 2021-09-26 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20210921_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='year',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.ManyToManyField(null=True, related_name='semester', to='course.Semester'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]