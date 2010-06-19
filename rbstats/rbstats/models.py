from django.contrib.auth.models import User
from django.db import models
from reviewboard.reviews.models import Review, ReviewRequest

class ReviewingSession(models.Model):
    review_request = models.ForeignKey(ReviewRequest, related_name="working_sessions", blank=False)
    user = models.ForeignKey(User, related_name="review_request_working_sessions", blank=False)
    review = models.OneToOneField(Review, related_name="working_session", blank=True)
    working_seconds = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("review_request", "user", "review")
