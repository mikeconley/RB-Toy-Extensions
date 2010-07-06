# Reports extension for Review Board.
from django.conf import settings
from django.conf.urls.defaults import patterns, include
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import DashboardHook, URLHook, TemplateHook
from reviewboard.reviews.signals import review_published


class RBStatsDashboardHook(DashboardHook):
    def get_entries(self):
        return [{
            'label': 'Statistics',
            'url': settings.SITE_ROOT + 'rbstats/',
        }]


class RBStatsExtension(Extension):
    
    is_configurable = True
    
    def __init__(self):
        Extension.__init__(self)
        self.dashboard_hook = RBStatsDashboardHook(self)
        self.url_hook = URLHook(self, patterns('',
            (r'^rbstats/', include('rbstats.urls'))))
