# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cereal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cereal_name', models.CharField(max_length=200, null=True, blank=True)),
                ('calories', models.IntegerField(null=True, blank=True)),
                ('protient', models.IntegerField(null=True, blank=True)),
                ('fat', models.IntegerField(null=True, blank=True)),
                ('sodium', models.IntegerField(null=True, blank=True)),
                ('dietary_fiber', models.IntegerField(null=True, blank=True)),
                ('carbs', models.IntegerField(null=True, blank=True)),
                ('sugars', models.IntegerField(null=True, blank=True)),
                ('potassium', models.IntegerField(null=True, blank=True)),
                ('vitamins_and_minerals', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='cereal',
            name='manufacturer',
            field=models.ForeignKey(to='main.Manufacturer'),
        ),
    ]
