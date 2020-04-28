# Generated by Django 3.0.5 on 2020-04-28 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200)),
                ('client_country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(max_length=200)),
                ('style_price', models.IntegerField(default=0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fichas.Client')),
            ],
        ),
    ]
