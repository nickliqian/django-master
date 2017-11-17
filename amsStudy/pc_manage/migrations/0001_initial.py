# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=50, verbose_name='\u4e3b\u673a\u540d')),
                ('base', models.CharField(max_length=100, verbose_name='\u673a\u623f')),
                ('location', models.CharField(max_length=50, verbose_name='\u673a\u67b6')),
                ('version', models.CharField(max_length=50, verbose_name='\u578b\u53f7')),
                ('memory', models.CharField(max_length=15, verbose_name='\u5185\u5b58')),
                ('disk', models.CharField(max_length=50, verbose_name='\u786c\u76d8')),
                ('cpu', models.CharField(max_length=50, verbose_name='CPU')),
                ('disk_array', models.CharField(max_length=50, verbose_name='\u786c\u76d8\u9635\u5217')),
                ('power', models.CharField(max_length=100, verbose_name='\u7535\u6e90')),
                ('extend_hardware', models.CharField(max_length=50, null=True, verbose_name='\u989d\u5916\u6dfb\u52a0', blank=True)),
                ('wan_ip', models.CharField(max_length=80, verbose_name='\u5916\u7f51IP')),
                ('Intranet_ip', models.CharField(max_length=80, verbose_name='\u5185\u7f51IP')),
                ('os', models.CharField(max_length=50, verbose_name='\u7cfb\u7edf\u7248\u672c')),
                ('usage', models.CharField(max_length=80, verbose_name='\u7528\u9014')),
                ('serial_number', models.CharField(max_length=100, verbose_name='\u5e8f\u5217\u53f7')),
                ('fixed_assets_encoding', models.CharField(max_length=100, verbose_name='\u56fa\u5b9a\u8d44\u4ea7\u7f16\u53f7')),
                ('ops_history', models.TextField(null=True, verbose_name='\u64cd\u4f5c\u5386\u53f2', blank=True)),
                ('comment', models.TextField(null=True, verbose_name='\u6ce8\u91ca', blank=True)),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668\u5217\u8868',
                'verbose_name_plural': '\u670d\u52a1\u5668\u5217\u8868',
            },
        ),
    ]
