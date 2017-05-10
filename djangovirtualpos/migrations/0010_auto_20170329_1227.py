# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangovirtualpos', '0009_vpsrefundoperation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vposrefundoperation',
            name='confirmation_code',
        ),
        migrations.AlterField(
            model_name='vposrefundoperation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], max_length=64, verbose_name='Estado de la devoluci\xf3n'),
        ),
    ]