from reviewboard.webapi.resources import WebAPIResource
from rbstats.models import ReviewingSession
from djblets.webapi.resources import register_resource_for_model

class ReviewingSessionResource(WebAPIResource):
    model = ReviewingSession
    name = 'reviewing-session'
    plural_name = 'reviewing-sessions'
    allowed_methods = ('GET')
    uri_object_key = 'id'
    fields = ('id')

reviewing_session_resource = ReviewingSessionResource()
register_resource_for_model(ReviewingSession, reviewing_session_resource)
