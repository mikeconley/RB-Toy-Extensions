import datetime


from django import template


register = template.Library()


@register.filter
def has_reviewing_session(review):
    """
    Returns whether or not this review has a reviewing session
    """
    try:
        return review.reviewing_session
    except Exception, e:
        # Hack alarm:  from here, I can't seem to import rbstats.models,
        # so I can't catch ReviewingSession.DoesNotExist.  This will
        # have to do.
        if str(e.__class__) == "<class 'rbstats.models.DoesNotExist'>":
            return False
        raise e


@register.filter
def seconds_to_duration(seconds):
    delta = datetime.timedelta(seconds=seconds)
    return str(delta)
