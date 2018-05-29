from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ssh.views',
    url(r'^$', 'index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'Login', name='login'),
    url(r'^logout/$', 'Logout', name='logout'),
    url(r'^asset_list$', 'asset_list', name='asset_list'),
    url(r'^asset_add/$', 'asset_add', name='asset_add'),
    url(r'^asset_del/$', 'asset_del', name='asset_del'),
    url(r'^asset_edit/$', 'asset_edit', name='asset_edit'),
    url(r'^web_terminal/$', 'web_terminal', name='web_terminal'),
    url(r'^user_add/$', 'user_add', name='user_add'),
    url(r'^key_down/$', 'key_down', name='key_down'),
    url(r'^user_list/$', 'user_list', name='user_list'),
    url(r'^user_del/$', 'user_del', name='user_del'),
    url(r'^host_add/$', 'host_add', name='host_add'),
    url(r'^host_list/$', 'host_list', name='host_list'),
    url(r'^host_edit/$', 'host_edit', name='host_edit'),
    url(r'^host_del/$', 'host_del', name='host_del'),
    url(r'^asset_excel_download/$', 'asset_excel_download', name='asset_excel_download'),
    url(r'^upload/$', 'upload', name='upload'),
    url(r'^download/$', 'download', name='download'),
    url(r'^file_del/$', 'file_del', name='file_del'),
    url(r'^file_edit/$', 'file_edit', name='file_edit'),
    url(r'^scrapys/', include('scrapys.urls')),
)
