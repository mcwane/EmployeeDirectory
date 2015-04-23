# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0006_auto_20150420_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persontest',
            name='email',
            field=models.EmailField(max_length=45, null=True),
        ),
    ]
