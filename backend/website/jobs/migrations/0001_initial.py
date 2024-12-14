# Generated by Django 5.1.4 on 2024-12-14 21:07

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='job_listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=500)),
                ('Experience_level', models.CharField(blank=True, choices=[('Entry-level', 'Entry-level'), ('Mid-level', 'Mid-level'), ('Senior-level', 'Senior-level'), ('Manager', 'Manager'), ('Leadership / CXO', 'Leadership / CXO')], default='None', max_length=300)),
                ('Employment_type', models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Contract', 'Contract'), ('Internship', 'Internship'), ('Freelance', 'Freelance')], default='Full-Time', max_length=300)),
                ('Work_Mode', models.CharField(choices=[('On-site', 'On-site'), ('Remote', 'Remote'), ('Hybrid', 'Hybrid')], default='On-site', max_length=300)),
                ('Job_Location', models.CharField(max_length=2000)),
                ('Years_of_Experience_Required', models.IntegerField()),
                ('Salary_Range', models.CharField(blank=True, default='None', max_length=2000, null=True)),
                ('Educational_Qualifications', models.CharField(blank=True, default='None', max_length=2000, null=True)),
                ('Certifications', models.CharField(blank=True, default='None', max_length=2000, null=True)),
                ('Other_Benefits', models.CharField(blank=True, default='None', max_length=2000, null=True)),
                ('Number_of_Openings', models.IntegerField(blank=True, default=-1)),
                ('Client_Name', models.CharField(blank=True, default='None', max_length=2000, null=True)),
                ('Client_Industry', models.CharField(max_length=2000)),
                ('Job_Description', tinymce.models.HTMLField()),
                ('Required_skills', models.ManyToManyField(related_name='job_listings', to='jobs.skill')),
            ],
        ),
    ]
