# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('states', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(default=b'', max_length=8)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200)),
                ('second_name', models.CharField(default=b'', max_length=200)),
                ('birth_date', models.DateTimeField(blank=True)),
                ('city', models.CharField(default=b'', max_length=500)),
                ('state', models.CharField(default=b'', max_length=500)),
                ('country', models.CharField(default=b'', max_length=500)),
                ('zip_code', models.IntegerField(default=0)),
                ('address', models.CharField(default=b'', max_length=500)),
                ('email', models.EmailField(default=b'', unique=True, max_length=500, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('competitor_num', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default=1, to='events.Category')),
                ('competition', models.ForeignKey(default=1, to='events.Competition')),
                ('competitor', models.ForeignKey(default=1, to='competitors.Competitor')),
                ('kit_state', models.ForeignKey(default=1, to='states.KitState')),
                ('register_state', models.ForeignKey(default=1, to='states.RegisterState')),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimeReg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('register', models.ForeignKey(default=1, to='competitors.Register')),
            ],
        ),
        migrations.AddField(
            model_name='authentication',
            name='competitor',
            field=models.ForeignKey(default=1, to='competitors.Competitor'),
        ),
    ]
