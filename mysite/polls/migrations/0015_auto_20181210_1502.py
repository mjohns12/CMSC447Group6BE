# Generated by Django 2.1.3 on 2018-12-10 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20181210_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='longitude',
            new_name='lon',
        ),
    ]