from django_consultants.views import *
from django.conf.urls import patterns, include, url

# https://docs.djangoproject.com/en/dev/howto/static-files/
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_consultants.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^$', main_page),

    # Login / Logout
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),

    # Web portal
    (r'^portal', include('portal.urls')),

    # Static content
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':  'static'}),
  
    url(r'^admin/', include(admin.site.urls)) 
    # https://docs.djangoproject.com/en/dev/howto/static-files/
    # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
