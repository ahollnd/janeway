# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-11 11:49
from __future__ import unicode_literals

import core.file_system
from django.db import migrations, models
import repository.models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0022_preprintfile_uploaded'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preprintversion',
            options={'ordering': ('-version', '-date_time', '-id')},
        ),
        migrations.AddField(
            model_name='preprintfile',
            name='mime_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]