# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='org_id',
            field=models.IntegerField(default=-1, verbose_name='Organization ID'),
        ),
    ]
