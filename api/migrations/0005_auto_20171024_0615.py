# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 06:15
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20171021_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truck',
            name='id',
        ),
        migrations.AlterField(
            model_name='truck',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
