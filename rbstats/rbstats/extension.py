# Reports extension for Review Board.
from django.conf import settings
from django.conf.urls.defaults import patterns, include
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import DashboardHook, URLHook, TemplateHook
from reviewboard.reviews.signals import review_published
from rbstats.models import ReviewingSession
from rbstats.resources import reviewing_session_resource

class RBStatsDashboardHook(DashboardHook):
    def get_entries(self):
        return [{
            'label': 'Statistics',
            'url': settings.SITE_ROOT + 'rbstats/',
        }]


class RBStatsExtension(Extension):
    
    is_configurable = True
    requirements = ['rbdefects.extension.RBDefectsExtension']
    resources = [reviewing_session_resource]
    
    def __init__(self):
        Extension.__init__(self)
        self.dashboard_hook = RBStatsDashboardHook(self)
        self.url_hook = URLHook(self, patterns('',
            (r'^rbstats/', include('rbstats.urls'))))
            
        self.activity_monitor = TemplateHook(self, "base-scripts-post", 
            "rbstats/activity_monitor.html", [
                'view_diff', 
                'view_diff_revision', 
                'view_screenshot',
            ]
        )
        
        self.mousewheel_lib = TemplateHook(self, "base-scripts",
            "rbstats/mousewheel_lib.html", [
                'view_diff',
                'view_diff_revision',
                'view_screenshot',
            ]
        )
        
        self.review_display = TemplateHook(self, "review-summary-header-post",
            "rbstats/review_summary_insert.html")

        
def on_review_published(sender, **kwargs):
    # Let's see if we can find the right ReviewingSession for this
    # user and review
    user = kwargs.get('user')
    review = kwargs.get('review')
    review_request = review.review_request
    review_session = ReviewingSession.objects.get(user=user, 
        review_request=review_request,review=None)
    
    review_session.review = review
    review_session.save()

review_published.connect(on_review_published)

