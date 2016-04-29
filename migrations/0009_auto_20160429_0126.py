# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitors', '0008_auto_20160427_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='address2',
            field=models.CharField(default=b'', max_length=500, blank=True),
        ),
    ]
