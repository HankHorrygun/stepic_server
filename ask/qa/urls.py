from django.conf.urls import patterns, include, url

from qa.views import get_404, test

urlpatterns = patterns(
    url(r'^(\d+)/$', test, name='test'),
)
