from django.conf.urls import patterns, include, url
from views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    #GET admin/
    url(r'^admin/', include(admin.site.urls)),

    #GET /
    url(r'^$', 'imentor.views.homepage', name = 'Landing'),

    #GET user/:id/messages/send/
    url(r'^user/(?P<user_id>\w+)/messages/(?P<message_id>\w+)/details/$', 'imentor.views.message_details'),

    url(r'^user/(?P<user_id>\w+)/messages/send/$', 'imentor.views.send_message'),

    #GET user/:id/messages/by_tag/
    url(r'^user/(?P<user_id>\w+)/messages/by_tag/$', 'imentor.views.retrieve_by_tags'),

    #GET user/:id/messages/
    url(r'^user/(?P<user_id>\w+)/messages/$', 'imentor.views.user_messages'),

    #GET user/:id/pairs/
    url(r'^user/(?P<user_id>\w+)/pairs/$', 'imentor.views.pc_pairs'),

    #GET user/:id/
    url(r'^user/(?P<user_id>\w+)/$', 'imentor.views.user_profile'),

)
