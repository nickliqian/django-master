# coding=utf-8
from django.contrib import admin
from models import ServerList


class SeverListAdmin(admin.ModelAdmin):
    site_header = 'AMS系统－请登录'  # 此处设置页面显示标题
    site_title = 'AMS系统'  # 此处设置页面头部标题

    # 显示字段
    list_display = (
        'hostname', 'base', 'location', 'version', 'memory', 'disk', 'cpu', 'disk_array', 'power', 'extend_hardware',
        )
    # 搜索字段
    search_fields = (
        'hostname', 'base', 'location', 'version', 'memory', 'disk', 'cpu', 'disk_array', 'power', 'extend_hardware',
        )
    # 每页条数
    list_per_page = 20
    # 指定填写表单时只包含某个字段
    # fields = ('location', 'base')
    # 可筛选字段
    list_filter = ('hostname', 'base',)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('hostname', 'base')
    # 设置默认排序字段，负号表示降序排序
    ordering = ('-hostname',)
    # 设置默认可编辑字段
    # list_editable = ['location', ]


admin.site.register(ServerList, SeverListAdmin)
