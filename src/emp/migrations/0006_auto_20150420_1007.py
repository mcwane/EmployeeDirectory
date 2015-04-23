# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0005_auto_20150420_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persontest',
            old_name='phone',
            new_name='Mobile',
        ),
        migrations.RemoveField(
            model_name='persontest',
            name='age',
        ),
        migrations.AddField(
            model_name='persontest',
            name='Address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='persontest',
            name='EmgContact',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='persontest',
            name='bloodgroup',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='persontest',
            name='email',
            field=models.EmailField(default=2, max_length=45),
            preserve_default=False,
        ),
    ]
