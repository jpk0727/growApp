"""urlconf for the base application"""

from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns('base.views',
    url(r'^$', 'home', name='home'),
    url(r'^monitor/$', 'monitor', name='monitor'),
    url(r'^about/$', 'about', name='about'),
    url(r'^control/$', 'control', name='control'),
)

