# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('competitors', '0007_register_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authentication',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
