# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pc_manage', '0002_auto_20171017_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverlist',
            name='Intranet_ip',
            field=models.CharField(max_length=80, verbose_name='\u5185\u7f51IP'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='base',
            field=models.CharField(max_length=100, verbose_name='\u673a\u623f'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='comment',
            field=models.TextField(null=True, verbose_name='\u6ce8\u91ca', blank=True),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='disk',
            field=models.CharField(max_length=50, verbose_name='\u786c\u76d8'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='disk_array',
            field=models.CharField(max_length=50, verbose_name='\u786c\u76d8\u9635\u5217'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='extend_hardware',
            field=models.CharField(max_length=50, null=True, verbose_name='\u989d\u5916\u6dfb\u52a0', blank=True),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='fixed_assets_encoding',
            field=models.CharField(max_length=100, verbose_name='\u56fa\u5b9a\u8d44\u4ea7\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='hostname',
            field=models.CharField(max_length=50, verbose_name='\u4e3b\u673a\u540d'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='location',
            field=models.CharField(max_length=50, verbose_name='\u673a\u67b6'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='memory',
            field=models.CharField(max_length=15, verbose_name='\u5185\u5b58'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='ops_history',
            field=models.TextField(null=True, verbose_name='\u64cd\u4f5c\u5386\u53f2', blank=True),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='os',
            field=models.CharField(max_length=50, verbose_name='\u7cfb\u7edf\u7248\u672c'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='power',
            field=models.CharField(max_length=100, verbose_name='\u7535\u6e90'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='serial_number',
            field=models.CharField(max_length=100, verbose_name='\u5e8f\u5217\u53f7'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='usage',
            field=models.CharField(max_length=80, verbose_name='\u7528\u9014'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='version',
            field=models.CharField(max_length=50, verbose_name='\u578b\u53f7'),
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='wan_ip',
            field=models.CharField(max_length=80, verbose_name='\u5916\u7f51IP'),
        ),
    ]
