# Generated by Django 3.2.6 on 2023-01-17 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Linked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('link', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('year', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchInterests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('paper_link', models.CharField(blank=True, max_length=50, null=True)),
                ('slide_link', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('course', models.CharField(blank=True, max_length=30)),
                ('graduate_year', models.CharField(blank=True, max_length=10)),
                ('email', models.CharField(blank=True, max_length=30)),
                ('pic', models.CharField(blank=True, max_length=20)),
                ('employment', models.CharField(blank=True, max_length=100)),
                ('linked', models.ManyToManyField(blank=True, related_name='master', to='member.Linked')),
                ('thesis', models.ManyToManyField(blank=True, related_name='master', to='member.Thesis')),
            ],
        ),
        migrations.CreateModel(
            name='Graduated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('course', models.CharField(blank=True, max_length=30)),
                ('admission_date', models.CharField(blank=True, max_length=10)),
                ('email', models.CharField(blank=True, max_length=30)),
                ('pic', models.CharField(blank=True, max_length=20)),
                ('linked', models.ManyToManyField(blank=True, related_name='graduated', to='member.Linked')),
                ('research_interests', models.ManyToManyField(blank=True, related_name='graduated', to='member.ResearchInterests')),
            ],
        ),
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('course', models.CharField(blank=True, max_length=30)),
                ('graduate_year', models.CharField(max_length=10, null=True)),
                ('project', models.ManyToManyField(blank=True, related_name='alumni', to='member.Project')),
                ('team', models.ManyToManyField(related_name='alumni', to='member.Team')),
            ],
        ),
    ]
