# Generated by Django 5.1.4 on 2025-01-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page_content', '0019_delete_ourstatisics_alter_stats_clientsserved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='CandidateSatisfactionRate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='CandidatesPlaced',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='ClientRetentionRate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='JoiningRatio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stats',
            name='TurnAroundTime',
            field=models.IntegerField(),
        ),
    ]
