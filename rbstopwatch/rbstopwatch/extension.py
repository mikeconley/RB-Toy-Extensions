# Reports extension for Review Board.
import datetime


from django.conf import settings
from django.conf.urls.defaults import patterns, include
from django.db.models import Sum
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import DashboardHook, URLHook, TemplateHook
from reviewboard.reviews.signals import review_published
from rbstats.hooks import RBStatsTableEntryHook
from rbstopwatch.models import ReviewingSession
from rbstopwatch.resources import reviewing_session_resource

class RBStopwatchStatsTableEntry(RBStatsTableEntryHook):
    def description_for_user(self):
        return "Reviewing Time"

    def for_user(self, user):
        all_reviewing_seconds = user.review_request_reviewing_sessions.aggregate(Sum('working_seconds'))['working_seconds__sum'] or 0
        total_reviewing_time = datetime.timedelta(seconds=all_reviewing_seconds)
        return str(total_reviewing_time)


class RBStopwatchExtension(Extension):

    is_configurable = True
    resources = [reviewing_session_resource]

    def __init__(self):
        Extension.__init__(self)
           
        self.activity_monitor = TemplateHook(self, "base-scripts-post", 
            "rbstopwatch/activity_monitor.html", [
                'view_diff', 
                'view_diff_revision', 
                'view_screenshot',
            ]
        )
        
        self.mousewheel_lib = TemplateHook(self, "base-scripts",
            "rbstopwatch/mousewheel_lib.html", [
                'view_diff',
                'view_diff_revision',
                'view_screenshot',
            ]
        )
        
        self.review_display = TemplateHook(self, "review-summary-header-post",
            "rbstopwatch/review_summary_insert.html")

        self.stats_hook = RBStopwatchStatsTableEntry(self)


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
