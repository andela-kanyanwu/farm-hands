# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_plan_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
