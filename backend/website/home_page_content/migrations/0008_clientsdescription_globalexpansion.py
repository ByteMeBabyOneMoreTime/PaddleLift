# Generated by Django 5.1.4 on 2024-12-21 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page_content', '0007_alter_organizationalstructure_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientsDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=4000)),
            ],
            options={
                'verbose_name': '5 - Clients Description',
            },
        ),
        migrations.CreateModel(
            name='GlobalExpansion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=4000)),
            ],
            options={
                'verbose_name': '4 - Global Expansion',
            },
        ),
    ]
