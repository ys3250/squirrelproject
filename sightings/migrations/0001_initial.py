# Generated by Django 2.2.7 on 2019-12-05 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('unique_squirrel_id', models.CharField(help_text='Unique Squirrel ID', max_length=100, primary_key=True, serialize=False, unique=True)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', help_text='AM/PM', max_length=2, null=True)),
                ('date', models.DateTimeField(help_text='Date', null=True)),
                ('age', models.CharField(help_text='Age', max_length=10, null=True)),
                ('latitude', models.FloatField(help_text='Latitude', max_length=20, null=True)),
                ('longitude', models.FloatField(help_text='Longtitude', max_length=20, null=True)),
                ('primary_fur_color', models.CharField(help_text='Primary Fur Color', max_length=100, null=True)),
                ('location', models.CharField(help_text='Location', max_length=100, null=True)),
                ('specific_location', models.CharField(help_text='Specific Location', max_length=100, null=True)),
                ('running', models.CharField(choices=[('true', 'true'), ('false', 'false'), ('', '')], default='', help_text='TRUE/FALSE', max_length=10, null=True)),
                ('chasing', models.CharField(choices=[('true', 'true'), ('false', 'false'), ('', '')], default='', help_text='TRUE/FALSE', max_length=10, null=True)),
                ('climbing', models.CharField(choices=[('true', 'true'), ('false', 'false'), ('', '')], default='', help_text='TRUE/FALSE', max_length=10, null=True)),
                ('eating', models.CharField(choices=[('true', 'true'), ('false', 'false'), ('', '')], default='', help_text='TRUE/FALSE', max_length=10, null=True)),
                ('foraging', models.CharField(choices=[('true', 'true'), ('false', 'false'), ('', '')], default='', help_text='TRUE/FALSE', max_length=10, null=True)),
                ('other_activities', models.CharField(help_text='Other Activities', max_length=100, null=True)),
                ('kuks', models.CharField(choices=[('true', 'true'), ('false', 'false'), ('', '')], default='', help_text='TRUE/FALSE', max_length=10, null=True)),
                ('quaas', models.CharField(choices=[('true', 'true'), ('false', 'false'), ('', '')], default='', help_text='TRUE/FALSE', max_length=10, null=True)),
                ('moans', models.CharField(choices=[('true', 'true'), ('false', 'false'), ('', '')], default='', help_text='TRUE/FALSE', max_length=10, null=True)),
                ('tail_flags', models.CharField(choices=[('true', 'true'), ('false', 'false'), ('', '')], default='', help_text='TRUE/FALSE', max_length=10, null=True)),
                ('tail_twitches', models.CharField(choices=[('true', 'true'), ('false', 'false'), ('', '')], default='', help_text='TRUE/FALSE', max_length=10, null=True)),
                ('approaches', models.CharField(choices=[('true', 'true'), ('false', 'false'), ('', '')], default='', help_text='TRUE/FALSE', max_length=10, null=True)),
                ('indifferent', models.CharField(choices=[('true', 'true'), ('false', 'false'), ('', '')], default='', help_text='TRUE/FALSE', max_length=10, null=True)),
                ('runs_from', models.CharField(choices=[('true', 'true'), ('false', 'false'), ('', '')], default='', help_text='TRUE/FALSE', max_length=10, null=True)),
            ],
        ),
    ]
