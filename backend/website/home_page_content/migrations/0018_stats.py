# Generated by Django 5.1.4 on 2025-01-15 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page_content', '0017_delete_ourstatistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=4000)),
                ('ClientsServed', models.CharField(max_length=4000)),
                ('CandidatesPlaced', models.CharField(max_length=4000)),
                ('ClientRetentionRate', models.CharField(max_length=4000)),
                ('TurnAroundTime', models.CharField(max_length=4000)),
                ('JoiningRatio', models.CharField(max_length=4000)),
                ('CandidateSatisfactionRate', models.CharField(max_length=4000)),
            ],
            options={
                'verbose_name': '3 - Stats',
            },
        ),
    ]
