# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitors', '0002_auto_20160113_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='birth_date',
            field=models.DateField(default=b'1992-05-05', blank=True),
        ),
    ]
