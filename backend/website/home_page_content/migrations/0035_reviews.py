# Generated by Django 5.1.4 on 2025-01-29 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page_content', '0034_contactinformation_fewsuccessstories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=400)),
                ('rating', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('date', models.CharField(max_length=200)),
            ],
        ),
    ]
