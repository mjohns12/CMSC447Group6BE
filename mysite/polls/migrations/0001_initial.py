# Generated by Django 2.1.3 on 2018-12-04 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallCenterOp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('branchName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipmentType', models.CharField(max_length=50)),
                ('numberAvailable', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('streetNum', models.CharField(max_length=30)),
                ('streetName', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zipCode', models.PositiveIntegerField()),
                ('phoneNumber', models.CharField(max_length=30)),
                ('timeCalleIn', models.DateTimeField()),
                ('description', models.CharField(max_length=30)),
                ('priorityCode', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EventStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('status', models.CharField(max_length=200)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Event')),
            ],
        ),
        migrations.CreateModel(
            name='FirstResponder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('branchName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=25)),
                ('location', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FirstResponderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OpChief',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('branchName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LeadFirstResponder',
            fields=[
                ('firstresponder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='polls.FirstResponder')),
            ],
            options={
                'abstract': False,
            },
            bases=('polls.firstresponder',),
        ),
        migrations.AddField(
            model_name='firstresponderstatus',
            name='firstResponder_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.FirstResponder'),
        ),
        migrations.AddField(
            model_name='firstresponder',
            name='missions',
            field=models.ManyToManyField(to='polls.Mission'),
        ),
        migrations.AddField(
            model_name='event',
            name='mission_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Mission'),
        ),
        migrations.AddField(
            model_name='event',
            name='opChief_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.OpChief'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='events',
            field=models.ManyToManyField(to='polls.Event'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='missions',
            field=models.ManyToManyField(to='polls.Mission'),
        ),
    ]