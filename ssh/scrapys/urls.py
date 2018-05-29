from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('scrapys.views',
    url(r'^fjob/$', 'fjob', name='fjob'),
    url(r'^index/$', 'index', name='scrapys_index'),
)
