# Generated by Django 2.2.5 on 2019-09-07 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobCode', models.TextField()),
                ('description', models.TextField()),
                ('hourlyRate', models.IntegerField()),
                ('maxHoursPerDay', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machineCode', models.TextField()),
                ('description', models.TextField()),
                ('hourlyRent', models.IntegerField()),
                ('maxHoursPerDay', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Timecard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteCode', models.TextField()),
                ('contractorName', models.TextField()),
                ('totalHours', models.IntegerField()),
                ('totalAmount', models.IntegerField()),
            ],
        ),
    ]
