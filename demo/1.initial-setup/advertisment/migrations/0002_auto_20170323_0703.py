# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('advertisment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='advert',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='advert',
            name='notes',
            field=models.TextField(default='notes'),
        ),
        migrations.AddField(
            model_name='advert',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='advertcategory',
            name='notes',
            field=models.CharField(default=datetime.datetime(2017, 3, 23, 7, 3, 14, 357642, tzinfo=utc), max_length=255, verbose_name='Notes'),
            preserve_default=False,
        ),
    ]
