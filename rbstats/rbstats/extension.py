# Reports extension for Review Board.
from django.conf import settings
from django.conf.urls.defaults import patterns, include
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import DashboardHook, URLHook


class RBStatsDashboardHook(DashboardHook):
    def get_entries(self):
        return [{
            'label': 'My Statistics',
            'url': settings.SITE_ROOT + 'stats/',
        }]


class RBStatsExtension(Extension):
    is_configurable = True
    requires = ['rbdefects.extension.RBDefectsExtension']

    def __init__(self):
        Extension.__init__(self)
        self.dashboard_hook = RBStatsDashboardHook(self)
