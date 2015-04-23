# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0004_auto_20150420_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persontest',
            name='department',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='persontest',
            name='designation',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
