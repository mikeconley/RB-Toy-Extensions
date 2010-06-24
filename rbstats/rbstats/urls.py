from django.conf.urls.defaults import patterns


urlpatterns = patterns('rbstats.views',
    (r'^$', 'rbstats_main'),
)
