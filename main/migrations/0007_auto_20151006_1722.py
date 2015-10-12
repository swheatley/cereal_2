# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20151006_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cereal',
            old_name='protien',
            new_name='protein',
        ),
    ]
