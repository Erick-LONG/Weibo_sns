# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-27 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20170727_0826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='followers',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='follow_list',
            field=models.ManyToManyField(blank=True, related_name='my_fans', to='app01.UserProfile', verbose_name='粉丝列表'),
        ),
    ]
