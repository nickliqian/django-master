# coding=utf-8
from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class ServerList(models.Model):
    hostname = models.CharField(max_length=50, verbose_name=u'主机名', help_text='Hello World!')
    base = models.CharField(max_length=100, verbose_name=u'机房')
    location = models.CharField(max_length=50, verbose_name=u'机架')
    version = models.CharField(max_length=50, verbose_name=u'型号')
    memory = models.CharField(max_length=15, verbose_name=u'内存')
    disk = models.CharField(max_length=50, verbose_name=u'硬盘')
    cpu = models.CharField(max_length=50, verbose_name=u'CPU')
    disk_array = models.CharField(max_length=50, verbose_name=u'硬盘阵列')
    power = models.CharField(max_length=100, verbose_name=u'电源')
    extend_hardware = models.CharField(max_length=50, blank=True, null=True, verbose_name=u'额外添加')
    wan_ip = models.CharField(max_length=80, verbose_name=u'外网IP')
    Intranet_ip = models.CharField(max_length=80, verbose_name=u'内网IP')
    os = models.CharField(max_length=50, verbose_name=u'系统版本')
    usage = models.CharField(max_length=80, verbose_name=u'用途')
    serial_number = models.CharField(max_length=100, verbose_name=u'序列号')
    fixed_assets_encoding = models.CharField(max_length=100, verbose_name=u'固定资产编号')
    ops_history = models.TextField(verbose_name=u'操作历史', blank=True, null=True)
    comment = models.TextField(verbose_name=u'注释', blank=True, null=True)

    # # 给特定字段加颜色
    # def colored_name(self):
    #     return format_html(
    #         '<span style="color: #{};">{} {}</span>',
    #         self.color_code,
    #         self.base,
    #     )

    def __str__(self):
        return u'Host:%s Room:%s Location:%s Type:%s' % (self.hostname, self.base, self.location, self.version)

    class Meta:
        verbose_name = u'服务器列表'
        verbose_name_plural = u'服务器列表'


class Students(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True)
    sorce = models.IntegerField(blank=True)
    room = models.ForeignKey('Room')

    def __str__(self):
        return u'Name:%s' % self.name

    class Meta:
        verbose_name = u'学生'
        verbose_name_plural = u'学生'


class Room(models.Model):
    room_num = models.CharField(max_length=255)
    room_size = models.IntegerField(blank=True)

    def __str__(self):
        return u'Room:%s' % self.room_num

    class Meta:
        verbose_name = u'班级'
        verbose_name_plural = u'班级'
