# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20151006_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cereal',
            old_name='protient',
            new_name='protien',
        ),
    ]
