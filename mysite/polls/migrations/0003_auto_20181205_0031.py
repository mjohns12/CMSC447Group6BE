# Generated by Django 2.1.3 on 2018-12-05 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20181204_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='city',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='event',
            name='firstName',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='event',
            name='lastName',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='mission_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Mission'),
        ),
        migrations.AlterField(
            model_name='event',
            name='opChief_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.OperationsChief'),
        ),
        migrations.AlterField(
            model_name='event',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='event',
            name='priorityCode',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='state',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='event',
            name='streetName',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='event',
            name='streetNum',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='event',
            name='timeCalleIn',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='zipCode',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
