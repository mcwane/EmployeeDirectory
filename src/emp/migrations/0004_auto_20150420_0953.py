# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0003_persontest_empid'),
    ]

    operations = [
        migrations.AddField(
            model_name='persontest',
            name='department',
            field=models.CharField(default=datetime.datetime(2015, 4, 20, 9, 53, 4, 558805, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persontest',
            name='designation',
            field=models.CharField(default=datetime.datetime(2015, 4, 20, 9, 53, 15, 998388, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persontest',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 20, 9, 53, 25, 101298, tzinfo=utc), verbose_name=b'Date', auto_now_add=True),
            preserve_default=False,
        ),
    ]
