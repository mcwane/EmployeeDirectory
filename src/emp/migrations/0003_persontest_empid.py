# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_auto_20150416_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='persontest',
            name='Empid',
            field=models.CharField(default=b'SampleEmpid', max_length=200),
        ),
    ]
