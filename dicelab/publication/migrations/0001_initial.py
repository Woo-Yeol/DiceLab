# Generated by Django 3.2.6 on 2023-01-17 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatentYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')], default='2023', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')], default='2023', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Patents',
            fields=[
                ('title', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=100, null=True)),
                ('num', models.CharField(max_length=100, null=True)),
                ('assign', models.CharField(max_length=100, null=True)),
                ('year', models.ManyToManyField(blank=True, related_name='patents', to='publication.PatentYear')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('title', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('label', models.CharField(choices=[('International_Paper', 'International_Paper'), ('Domestic_Paper', 'Domestic_Paper')], default='International_Paper', max_length=20)),
                ('paper_link', models.CharField(max_length=100, null=True)),
                ('thesis', models.CharField(max_length=100, null=True)),
                ('assign', models.CharField(max_length=100, null=True)),
                ('year', models.ManyToManyField(blank=True, related_name='paper', to='publication.Year')),
            ],
        ),
    ]
