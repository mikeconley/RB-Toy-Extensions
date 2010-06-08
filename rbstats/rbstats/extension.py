# Reports extension for Review Board.
from django.conf import settings
from django.conf.urls.defaults import patterns, include
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import DashboardHook, URLHook, TemplateHook
from rbstats.resources import reviewing_session_resource

class RBStatsDashboardHook(DashboardHook):
    def get_entries(self):
        return [{
            'label': 'My Statistics',
            'url': settings.SITE_ROOT + 'stats/',
        }]


class RBStatsExtension(Extension):
    
    is_configurable = True
    requires = ['rbdefects.extension.RBDefectsExtension']
    resources = [reviewing_session_resource]
    
    def __init__(self):
        Extension.__init__(self)
        self.dashboard_hook = RBStatsDashboardHook(self)
        #TemplateHook(self, "base-scripts-post", "bears/bears.html", ['dashboard'])
