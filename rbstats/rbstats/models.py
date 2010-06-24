from django.contrib.auth.models import User
from django.db import models
from reviewboard.reviews.models import Review, ReviewRequest
from datetime import datetime

class ReviewingSession(models.Model):
    review_request = models.ForeignKey(ReviewRequest,
        related_name="reviewing_sessions", blank=False)
    user = models.ForeignKey(User,
        related_name="review_request_reviewing_sessions", blank=False)
    review = models.OneToOneField(Review, related_name="reviewing_session",
        blank=True, null=True)
    last_updated = models.DateTimeField(default=datetime.now, auto_now=True,
        blank=False)
    working_seconds = models.PositiveIntegerField(default=0, blank=False)
