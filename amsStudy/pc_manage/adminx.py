#coding=utf-8
from __future__ import absolute_import
import xadmin
from xadmin import views
from .models import ServerList
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction


class MainDashboard(object):
    widgets = [
        [
            {"type": "html", "title": "Test Widget",
             "content": "<h3> Welcome to Xadmin! </h3><p>Join Online Group: <br/>QQ Qun : 282936295</p>"},
            {"type": "chart", "model": "app.accessrecord", "chart": "user_count",
             "params": {"_p_date__gte": "2013-01-08", "p": 1, "_p_date__lt": "2013-01-29"}},
            {"type": "list", "model": "app.host", "params": {"o": "-guarantee_date"}},
        ],
        [
            {"type": "qbutton", "title": "Quick Start",
             "btns": [{"model": ServerList}, {"model": ServerList}, {"title": "Google", "url": "http://www.google.com"}]},
            {"type": "addform", "model": ServerList},
        ]
    ]



class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class ServerListAdmin(object):
    list_display = (
        'hostname', 'base', 'location', 'version', 'memory', 'disk', 'cpu', 'disk_array', 'power', 'extend_hardware',
        'wan_ip', 'Intranet_ip', 'os', 'usage', 'serial_number', 'fixed_assets_encoding', 'ops_history', 'comment')

    list_display_links = ("hostname",)

    search_fields = ['hostname', 'base', 'location', 'version', 'memory',]
    style_fields = {"base": "checkbox-inline"}


xadmin.site.register(views.website.IndexView, MainDashboard)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(ServerList, ServerListAdmin)
# xadmin.sites.site.register(HostGroup, HostGroupAdmin)
# xadmin.sites.site.register(ServerList, ServerListAdmin)

# xadmin.sites.site.register(HostGroup, HostGroupAdmin)
# xadmin.sites.site.register(MaintainLog, MaintainLogAdmin)
# xadmin.sites.site.register(IDC, IDCAdmin)
# xadmin.sites.site.register(AccessRecord, AccessRecordAdmin)