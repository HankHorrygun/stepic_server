from django.conf.urls import patterns, include, url

from qa.views import get_404, test
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', get_404, name='root'),
    url(r'^login/$', get_404, name=''),
    url(r'^signup/$', get_404, name='signup'),
    url(r'^question/', include('qa.urls'), name='question'),
    url(r'^ask/$', get_404, name='ask'),
    url(r'^popular/$', get_404, name='popular'),
    url(r'^new/$', get_404, name='new'),
    url(r'^admin/', include(admin.site.urls)),
)
