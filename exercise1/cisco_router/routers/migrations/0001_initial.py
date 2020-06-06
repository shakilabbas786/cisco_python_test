# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Routers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sapid', models.CharField(max_length=50, null=True, blank=True)),
                ('hostname', models.CharField(max_length=50, null=True, blank=True)),
                ('loopback', models.CharField(max_length=50, null=True, blank=True)),
                ('macaddress', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'cisco_routers',
            },
        ),
    ]
