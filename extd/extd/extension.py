# Reports extension for Review Board.
from django.conf import settings
from django.conf.urls.defaults import patterns, include
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import DashboardHook, URLHook


class ExtDDashboardHook(DashboardHook):
    def get_entries(self):
        return [{
            'label': 'Ext-D',
            'url': settings.SITE_ROOT + 'exta/',
        }]


class ExtDExtension(Extension):
    is_configurable = True

    def __init__(self):
        Extension.__init__(self)
        self.dashboard_hook = ExtDDashboardHook(self)
