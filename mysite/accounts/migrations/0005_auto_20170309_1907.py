# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170309_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subjectID',
            field=models.CharField(default='Fs1LbD', max_length=6, null=True, unique=True),
        ),
    ]
