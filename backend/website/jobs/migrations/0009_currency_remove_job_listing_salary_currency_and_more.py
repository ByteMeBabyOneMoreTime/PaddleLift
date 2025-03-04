# Generated by Django 5.1.4 on 2025-02-28 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_job_listing_salary_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign', models.CharField(max_length=400, verbose_name='Currency')),
            ],
        ),
        migrations.RemoveField(
            model_name='job_listing',
            name='Salary_currency',
        ),
        migrations.AlterField(
            model_name='job_listing',
            name='Number_of_Openings',
            field=models.PositiveIntegerField(default=0, help_text='only positive integers allowed', verbose_name='Number of Openings'),
        ),
    ]
