# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 23:54
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judicial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='providencia',
            name='archivo',
            field=models.FileField(blank=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='asesorjuridico',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='providencia',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
