# Generated by Django 2.1.3 on 2018-12-08 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20181207_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstresponder',
            name='assignedMissionID',
            field=models.ManyToManyField(blank=True, null=True, to='polls.Mission'),
        ),
    ]
