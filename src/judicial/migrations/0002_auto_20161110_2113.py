# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-10 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('judicial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='asesorjuridico',
            options={},
        ),
        migrations.AlterModelManagers(
            name='asesorjuridico',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='asesorjuridico',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='asesorjuridico',
            name='email',
        ),
        migrations.RemoveField(
            model_name='asesorjuridico',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='asesorjuridico',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='asesorjuridico',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='asesorjuridico',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='asesorjuridico',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='asesorjuridico',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='asesorjuridico',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='asesorjuridico',
            name='password',
        ),
        migrations.RemoveField(
            model_name='asesorjuridico',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='asesorjuridico',
            name='username',
        ),
        migrations.RemoveField(
            model_name='documento',
            name='url',
        ),
        migrations.AddField(
            model_name='dictamen',
            name='numero_instancia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documento',
            name='archivo',
            field=models.FileField(blank=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='expedientejuridico',
            name='numero_instancia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='opinionjuridica',
            name='numero_instancia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='providencia',
            name='numero_instancia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dictamen',
            name='asesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judicial.AsesorJuridico'),
        ),
        migrations.AlterField(
            model_name='dictamen',
            name='fecha_emision',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='ultima_modificacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='expedientejuridico',
            name='solicitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judicial.AsesorJuridico'),
        ),
        migrations.AlterField(
            model_name='opinionjuridica',
            name='asesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judicial.AsesorJuridico'),
        ),
        migrations.AlterField(
            model_name='opinionjuridica',
            name='fecha_emision',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='expedientejuridico',
            name='expediente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='judicial.Expediente'),
        ),
    ]
