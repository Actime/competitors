# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
    ]
