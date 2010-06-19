# Reports extension for Review Board.
from django.conf import settings
from django.conf.urls.defaults import patterns, include
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import DashboardHook, URLHook


class ExtCDashboardHook(DashboardHook):
    def get_entries(self):
        return [{
            'label': 'Ext-C',
            'url': settings.SITE_ROOT + 'exta/',
        }]


class ExtCExtension(Extension):
    is_configurable = True
    requirements = ['extb.extension.ExtBExtension', 'exta.extension.ExtAExtension']

    def __init__(self):
        Extension.__init__(self)
        self.dashboard_hook = ExtCDashboardHook(self)
