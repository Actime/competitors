# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('competitors', '0003_auto_20160113_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitor',
            name='address2',
            field=models.CharField(default=b'', max_length=500),
        ),
        migrations.AddField(
            model_name='competitor',
            name='phone_number',
            field=models.CharField(default=b'', max_length=200, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b'N\xc3\xbamero de tel\xc3\xa9fono incorrecto.')]),
        ),
        migrations.AddField(
            model_name='competitor',
            name='sex',
            field=models.IntegerField(default=0, choices=[(0, b'M'), (1, b'F')]),
        ),
    ]
