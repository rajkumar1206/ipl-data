# Generated by Django 3.1.3 on 2020-11-24 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='match_won',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='match_won', to='teams.team'),
        ),
        migrations.AddField(
            model_name='matches',
            name='team_one',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='team_one', to='teams.team'),
        ),
        migrations.AddField(
            model_name='matches',
            name='team_two',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='team_two', to='teams.team'),
        ),
        migrations.AddField(
            model_name='matches',
            name='toss',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='toss', to='teams.team'),
        ),
        migrations.AddField(
            model_name='matches',
            name='year',
            field=models.ForeignKey(default=2020, on_delete=django.db.models.deletion.CASCADE, to='matches.iplseason'),
        ),
    ]
