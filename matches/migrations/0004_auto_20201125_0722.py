# Generated by Django 3.1.3 on 2020-11-25 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_auto_20201124_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='match_won_txt',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='matches',
            name='toss_txt',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='matches',
            name='team_one_txt',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='matches',
            name='team_two_txt',
            field=models.CharField(default='', max_length=10),
        ),
    ]
