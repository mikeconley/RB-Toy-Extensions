from reviewboard.extensions.base import Extension
from rbstats.hooks import RBStatsTableEntryHook

class RBKarmaStatsTableEntry(RBStatsTableEntryHook):
    def description_for_user(self):
        return "Karma"

    def for_user(self, user):
        total_review_requests = user.review_requests.count()
        total_reviews = user.reviews.count()
        review_karma = round(float(total_reviews) /
            float(total_review_requests), 4)
        return str(review_karma)


class RBKarmaExtension(Extension):

    is_configurable = True

    def __init__(self):
        Extension.__init__(self)
        self.stats_hook = RBKarmaStatsTableEntry(self)
