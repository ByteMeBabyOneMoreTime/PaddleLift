# Generated by Django 5.1.4 on 2025-01-24 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page_content', '0025_about_missionandvision'),
    ]

    operations = [
        migrations.RenameField(
            model_name='missionandvision',
            old_name='vision_description',
            new_name='vission_description',
        ),
        migrations.RenameField(
            model_name='missionandvision',
            old_name='vision_image_url',
            new_name='vission_image_url',
        ),
    ]
