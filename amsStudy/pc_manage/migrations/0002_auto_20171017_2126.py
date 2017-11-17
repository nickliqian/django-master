# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pc_manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverlist',
            name='Intranet_ip',
            field=models.CharField(max_length=80, verbose_name=b'\xe5\x86\x85\xe7\xbd\x91IP'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='base',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\x9c\xba\xe6\x88\xbf'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='comment',
            field=models.TextField(null=True, verbose_name=b'\xe6\xb3\xa8\xe9\x87\x8a', blank=True),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='disk',
            field=models.CharField(max_length=50, verbose_name=b'\xe7\xa1\xac\xe7\x9b\x98'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='disk_array',
            field=models.CharField(max_length=50, verbose_name=b'\xe7\xa1\xac\xe7\x9b\x98\xe9\x98\xb5\xe5\x88\x97'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='extend_hardware',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe9\xa2\x9d\xe5\xa4\x96\xe6\xb7\xbb\xe5\x8a\xa0', blank=True),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='fixed_assets_encoding',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x9b\xba\xe5\xae\x9a\xe8\xb5\x84\xe4\xba\xa7\xe7\xbc\x96\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='hostname',
            field=models.CharField(max_length=50, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='location',
            field=models.CharField(max_length=50, verbose_name=b'\xe6\x9c\xba\xe6\x9e\xb6'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='memory',
            field=models.CharField(max_length=15, verbose_name=b'\xe5\x86\x85\xe5\xad\x98'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='ops_history',
            field=models.TextField(null=True, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe5\x8e\x86\xe5\x8f\xb2', blank=True),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='os',
            field=models.CharField(max_length=50, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe7\x89\x88\xe6\x9c\xac'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='power',
            field=models.CharField(max_length=100, verbose_name=b'\xe7\x94\xb5\xe6\xba\x90'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='serial_number',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\xba\x8f\xe5\x88\x97\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='usage',
            field=models.CharField(max_length=80, verbose_name=b'\xe7\x94\xa8\xe9\x80\x94'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='version',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\x9e\x8b\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='wan_ip',
            field=models.CharField(max_length=80, verbose_name=b'\xe5\xa4\x96\xe7\xbd\x91IP'),
        ),
    ]
