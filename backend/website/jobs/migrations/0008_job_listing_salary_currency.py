# Generated by Django 5.1.4 on 2025-02-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_alter_job_listing_certifications_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_listing',
            name='Salary_currency',
            field=models.CharField(default='₹', max_length=400, verbose_name='Currency'),
        ),
    ]
