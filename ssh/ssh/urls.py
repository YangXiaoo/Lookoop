from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ssh.views',
    url(r'^$', 'index', name='index'),
    url(r'^login/$', 'Login', name='login'),
    url(r'^logout/$', 'Logout', name='logout'),
    url(r'^asset_list$', 'asset_list', name='asset_list'),
    url(r'^asset_add/$', 'asset_add', name='asset_add'),
    url(r'^asset_del/$', 'asset_del', name='asset_del'),
    url(r'^asset_edit/$', 'asset_edit', name='asset_edit'),
    url(r'^web_terminal/$', 'web_terminal', name='web_terminal'),
    url(r'^user_add/$', 'user_add', name='user_add'),
    url(r'^key_down/$', 'key_down', name='key_down'),
)
