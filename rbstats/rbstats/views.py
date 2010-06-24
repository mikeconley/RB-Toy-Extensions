import datetime
from django.db.models import Sum
from django.template.context import RequestContext
from django.shortcuts import render_to_response

def rbstats_main(request,
                template_name='rbstats/rbstats_main.html'):
    user = request.user
    total_review_requests = user.review_requests.count()
    total_reviews = user.reviews.count()
    review_karma = round(float(total_reviews) / 
        float(total_review_requests), 4)
    total_reviewing_seconds = user.review_request_reviewing_sessions.aggregate(Sum('working_seconds'))['working_seconds__sum']
    total_reviewing_time = datetime.timedelta(seconds=total_reviewing_seconds)
    
    return render_to_response(template_name, RequestContext(request, {
        'total_review_requests': total_review_requests,
        'total_reviews': total_reviews,
        'review_karma': review_karma,
        'total_reviewing_time': total_reviewing_time,       
    }))
