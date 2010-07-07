import datetime
from django.db.models import Sum
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from rbstats.hooks import RBStatsTableEntryHook

def rbstats_main(request,
                template_name='rbstats/rbstats_main.html'):
    user = request.user
    total_review_requests = user.review_requests.count()
    total_reviews = user.reviews.count()

    return render_to_response(template_name, RequestContext(request, {
        'total_review_requests': total_review_requests,
        'total_reviews': total_reviews,
        'table_hook_entries': RBStatsTableEntryHook.hooks,
    }))
