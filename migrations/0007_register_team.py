# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitors', '0006_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='team',
            field=models.ForeignKey(default=1, to='competitors.Team'),
        ),
    ]
