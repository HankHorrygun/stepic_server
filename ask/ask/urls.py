from django.conf.urls import patterns, include, url

from qa.views import get_404, test
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', test, name='root'),
    url(r'^login/.*$', test, name=''),
    url(r'^signup/.*$', test, name='signup'),
    url(r'^question/.*', include('qa.urls'), name='question'),
    url(r'^ask/.*$', test, name='ask'),
    url(r'^popular/.*$', test, name='popular'),
    url(r'^new/.*$', test, name='new'),
    url(r'^admin/', include(admin.site.urls)),
)
