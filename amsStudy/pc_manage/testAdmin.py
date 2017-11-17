# -*- coding: UTF-8 -*-
#coding=utf-8
from django.contrib import admin
from models import ServerList
from django.utils.translation import ugettext_lazy as _

class BaseListFilter(admin.SimpleListFilter):
    title = _(u'机房')
    parameter_name = 'base'

    def lookups(self, request, model_admin):
        return (
            ('1', _(u'一号')),
            ('6', _(u'六号')),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(age='１')
        if self.value() == '1':
            return queryset.filter(age__gte='18', age__lte='50')
        if self.value() == '2':
            return queryset.filter(age='6')

class SeverListAdmin(admin.ModelAdmin):
    site_header = 'AMS系统－请登录'  # 此处设置页面显示标题
    site_title = 'AMS系统'  # 此处设置页面头部标题

    list_display = (
    'hostname', 'base', 'location', 'version', 'memory', 'disk', 'cpu', 'disk_array', 'power', 'extend_hardware',
    'wan_ip', 'Intranet_ip', 'os', 'usage', 'serial_number', 'fixed_assets_encoding', 'ops_history', 'comment')
    search_fields = (
    'hostname', 'base', 'location', 'version', 'memory', 'disk', 'cpu', 'disk_array', 'power', 'extend_hardware',
    'wan_ip', 'Intranet_ip', 'os', 'usage', 'serial_number', 'fixed_assets_encoding')
    list_per_page = 20

    #　指定填写表单时只包含某个字段
    fields = ('location', 'base')
    exclude = ('hostname',)

    list_filter = ('hostname','base',BaseListFilter,)

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('hostname', 'base')
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-hostname',)

    # list_editable 设置默认可编辑字段
    list_editable = ['location',]

    # 详细时间分层筛选　
    # date_hierarchy = 'go_time'
    #一般ManyToManyField多对多字段用过滤器；标题等文本字段用搜索框；日期时间用分层筛选。
    #过滤器如果是外键需要遵循这样的语法：本表字段__外键表要显示的字段。如：“user__user_name”


    # fk_fields 设置显示外键字段
    # fk_fields = ('machine_room_id',)

    # 属性分组
    # fieldsets = [
    #     ('basic', {'fields': ['btitle']}),
    #     ('more', {'fields': ['bpub_date']}),
    # ]

    # list_filter = (('birthday', DateRangeFilter),)
    # gender.short_description = '性别'





admin.site.register(ServerList,SeverListAdmin)
# admin.admin_site.register = SeverListAdmin(name='management')