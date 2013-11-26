from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'swapbot.home.index', name='donation'),
    url(r'^index.html', 'swapbot.home.index',name='homepage'),
    # whatsthis
    url(r'^testing/', include('testing.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #properly redirect logins to login package...
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
