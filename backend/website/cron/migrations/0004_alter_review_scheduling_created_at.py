# Generated by Django 5.1.4 on 2025-01-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cron', '0003_alter_review_scheduling_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review_scheduling',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
