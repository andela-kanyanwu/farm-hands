# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160220_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='google_id',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
