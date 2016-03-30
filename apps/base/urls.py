"""urlconf for the base application"""

from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns('base.views',
    url(r'^$', 'home', name='home'),
    url(r'^grow/monitor/$', 'monitor', name='monitor'),
    url(r'^grow/about/$', 'about', name='about'),
    url(r'^grow/control/$', 'control', name='control'),
)

