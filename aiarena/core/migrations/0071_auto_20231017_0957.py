# Generated by Django 3.2.16 on 2023-10-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_competition_indepth_bot_statistics_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchparticipation',
            name='participant_number',
            field=models.PositiveSmallIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
