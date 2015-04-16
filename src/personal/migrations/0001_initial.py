# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(help_text=b'Their first name', max_length=60)),
                ('last_name', models.CharField(help_text=b'Do you know it?', max_length=80, blank=True)),
                ('birtday', models.DateField()),
            ],
        ),
    ]
