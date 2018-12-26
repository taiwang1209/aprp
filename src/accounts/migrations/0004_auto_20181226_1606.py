# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-26 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userinformation_reporter'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='alert_viewer',
            field=models.BooleanField(default=True, verbose_name='Alert Viewer'),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='monitor_info_viewer',
            field=models.BooleanField(default=True, verbose_name='Monitor Info Viewer'),
        ),
    ]
