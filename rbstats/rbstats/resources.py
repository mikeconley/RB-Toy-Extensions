from reviewboard.webapi.resources import WebAPIResource

from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist

from djblets.webapi.errors import DOES_NOT_EXIST
from djblets.webapi.resources import register_resource_for_model
from djblets.webapi.core import WebAPIResponse
from rbstats.models import ReviewingSession
from rbstats.settings import WAIT_SECONDS
from reviewboard.reviews.models import ReviewRequest
from reviewboard.webapi.decorators import webapi_check_login_required


class ReviewingSessionActivityResource(WebAPIResource):
    name = 'activity'
    name_plural = 'activity'
    allowed_methods = ('PUT',)
    
    @webapi_check_login_required
    def update(self, request, *args, **kwargs):

        try:
            reviewing_session = \
                reviewing_session_resource.get_object(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return DOES_NOT_EXIST

        time_since = datetime.now() - reviewing_session.last_updated
        
        if time_since.seconds < WAIT_SECONDS:
            return WebAPIResponse(request, status=304)
        else:
            reviewing_session.working_seconds += WAIT_SECONDS
            reviewing_session.last_updated = datetime.now()
            reviewing_session.save()

        return 200, {}

reviewing_session_activity_resource = ReviewingSessionActivityResource()


class ReviewingSessionResource(WebAPIResource):
    model = ReviewingSession
    name = 'reviewing-session'
    plural_name = 'reviewing-sessions'
    allowed_methods = ('GET', 'PUT')
    uri_object_key = 'id'
    fields = ('id')

    item_child_resources = [
        reviewing_session_activity_resource,
    ]
    
    def get(self, request, *args, **kwargs):
        review_session = self.get_object(request, *args, **kwargs)

        return 200, {
            self.item_result_key: {
                'last_updated': review_session.last_updated,
                'review_id': review_session.review_id,
                'review_request_id': review_session.review_request_id,
            }
        }
    
    def get_object(self, request, *args, **kwargs):
        review_request_id = kwargs.get('id')
        review_request = ReviewRequest.objects.get(id=review_request_id)
        review_session, created = self.model.objects.get_or_create(
            user=request.user, review_request=review_request,review=None)
        return review_session    

    
reviewing_session_resource = ReviewingSessionResource()
register_resource_for_model(ReviewingSession, reviewing_session_resource)
