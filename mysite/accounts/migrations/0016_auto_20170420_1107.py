# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 11:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20170420_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
