# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='权限名称')),
                ('url', models.CharField(max_length=255, verbose_name='URL名称')),
                ('per_method', models.SmallIntegerField(choices=[(1, 'GET'), (2, 'POST')], default=1, verbose_name='请求方法')),
                ('argument_list', models.CharField(blank=True, help_text='多个参数之间用英文半角逗号隔开', max_length=255, null=True, verbose_name='参数列表')),
                ('describe', models.CharField(max_length=255, verbose_name='描述')),
            ],
            options={
                'permissions': (('views_student_list', '查看学员信息表'), ('views_student_info', '查看学员详细信息')),
                'verbose_name': '权限表',
                'verbose_name_plural': '权限表',
            },
        ),
    ]
