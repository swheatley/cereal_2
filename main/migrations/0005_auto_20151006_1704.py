# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20151006_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cereal',
            name='dietary_fiber',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='manufacturer',
            field=models.ForeignKey(blank=True, to='main.Manufacturer', null=True),
        ),
    ]
