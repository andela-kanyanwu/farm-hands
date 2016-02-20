# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('farm_size', models.CharField(max_length=30, choices=[(b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large')])),
                ('weather', models.CharField(max_length=200)),
                ('crop_type', models.CharField(max_length=200)),
                ('budget', models.DecimalField(max_digits=8, decimal_places=2)),
                ('duration', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('cycle_type', models.CharField(max_length=30, choices=[(b'DAILY', b'daily'), (b'BIWEEKLY', b'biweekly'), (b'MONTHLY', b'monthly'), (b'YEARLY', b'yearly')])),
                ('desc', models.CharField(max_length=200)),
                ('plan', models.ForeignKey(related_name='schedule', to='api.Plan')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('google_id', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
