# Generated by Django 3.1.3 on 2020-11-25 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_player_team_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='year',
            field=models.IntegerField(default=2020),
        ),
    ]
