# Generated by Django 3.0.5 on 2020-04-30 14:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 30, 14, 50, 44, 981040, tzinfo=utc), verbose_name='date published'),
        ),
    ]
