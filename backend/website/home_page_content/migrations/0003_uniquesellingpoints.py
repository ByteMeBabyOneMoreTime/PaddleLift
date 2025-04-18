# Generated by Django 5.1.4 on 2024-12-21 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page_content', '0002_service_service2_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueSellingPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=5000)),
                ('service1_heading', models.CharField(default='', max_length=2500)),
                ('service1_description', models.CharField(default='', max_length=2500)),
                ('service2_heading', models.CharField(default='', max_length=2500)),
                ('service2_description', models.CharField(default='', max_length=2500)),
                ('service3_heading', models.CharField(default='', max_length=2500)),
                ('service3_description', models.CharField(default='', max_length=2500)),
                ('service4_heading', models.CharField(default='', max_length=2500)),
                ('service4_description', models.CharField(default='', max_length=2500)),
                ('image_url', models.URLField(default='', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
