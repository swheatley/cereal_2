# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20151006_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cereal',
            name='carbs',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
