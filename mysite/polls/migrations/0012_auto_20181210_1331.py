# Generated by Django 2.1.3 on 2018-12-10 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20181208_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketType', models.CharField(blank=True, max_length=30, null=True)),
                ('ticketStatus', models.CharField(blank=True, max_length=30, null=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Event')),
            ],
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='missions',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='events',
            field=models.ManyToManyField(blank=True, to='polls.Event'),
        ),
        migrations.AlterField(
            model_name='firstresponder',
            name='assignedMissionID',
            field=models.ManyToManyField(blank=True, to='polls.Mission'),
        ),
    ]