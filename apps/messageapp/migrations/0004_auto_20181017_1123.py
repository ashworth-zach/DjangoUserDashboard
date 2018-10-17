# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-17 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('messageapp', '0003_auto_20181017_0904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='users.User'),
            preserve_default=False,
        ),
    ]
