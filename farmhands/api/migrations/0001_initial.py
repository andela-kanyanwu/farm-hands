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
            name='Crop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('climate', models.CharField(max_length=30, choices=[(b'W', b'Tropical Wet'), (b'MO', b'Monsoon'), (b'S', b'Savanna'), (b'A', b'Arid'), (b'SA', b'Semi Arid'), (b'ME', b'Mediterranean'), (b'HS', b'Humid Subtropical'), (b'MA', b'Marine'), (b'WS', b'Warm Summer'), (b'CS', b'Cool Summer'), (b'B', b'Boreal'), (b'T', b'Tundra'), (b'I', b'Ice cap')])),
                ('crop_categories', models.CharField(max_length=30, choices=[(b'FOOD', b'Food'), (b'FEED', b'Feed'), (b'FIBRE', b'Fibre'), (b'OIL', b'Oil'), (b'ORNAMENTAL', b'Ornamental'), (b'INDUSTRIAL', b'Industrial')])),
                ('life_cycle', models.CharField(max_length=30, choices=[(b'ANNUAL', b'Annual'), (b'BIENNAL', b'Biennal'), (b'PERENNIAL', b'Perennial'), (b'EPHEMERALS', b'Ephemerals')])),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('desc', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('farm_size', models.CharField(max_length=30, choices=[(b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large')])),
                ('budget', models.DecimalField(max_digits=8, decimal_places=2)),
                ('duration', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('crop', models.ForeignKey(related_name='plan', to='api.Crop')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
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
                ('google_id', models.CharField(max_length=200, null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
