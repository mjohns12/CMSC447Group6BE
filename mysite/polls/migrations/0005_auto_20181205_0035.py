# Generated by Django 2.1.3 on 2018-12-05 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20181205_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
