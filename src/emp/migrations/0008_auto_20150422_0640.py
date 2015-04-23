# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0007_auto_20150421_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persontest',
            name='dob',
            field=models.DateField(auto_now_add=True, verbose_name=b'Date'),
        ),
    ]
