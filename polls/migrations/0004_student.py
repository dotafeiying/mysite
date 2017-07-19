# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170718_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='姓名')),
                ('age', models.SmallIntegerField(verbose_name='年龄')),
                ('sex', models.SmallIntegerField(choices=[(1, '男'), (2, '女'), (3, '未知')], verbose_name='性别')),
            ],
        ),
    ]
