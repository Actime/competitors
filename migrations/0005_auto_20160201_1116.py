# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitors', '0004_auto_20160201_0611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authentication',
            name='password',
        ),
        migrations.AddField(
            model_name='authentication',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
