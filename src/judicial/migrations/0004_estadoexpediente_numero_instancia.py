# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-11 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judicial', '0003_auto_20161111_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadoexpediente',
            name='numero_instancia',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
