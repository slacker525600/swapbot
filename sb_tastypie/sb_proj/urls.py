from django.conf.urls import patterns, include, url

from django.contrib import admin
from tastypie.api import Api
from swapbot.api import *
from swapbot import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(ItemResource())
v1_api.register(UserProfile())
v1_api.register(DonorResource())
v1_api.register(DonationResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sb_proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
