# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_auto_20160920_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='nasa_id',
        ),
        migrations.RemoveField(
            model_name='rover',
            name='nasa_id',
        ),
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='rover',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]