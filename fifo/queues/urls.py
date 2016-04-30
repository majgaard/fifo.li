# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
       url(
        regex=r'^all/$',
        view=views.all_queues,
        name='all_queues'
    ),
    url(
        regex=r'^active/$',
        view=views.active_queues,
        name='active_queues'
    ),
    url(
        regex=r'^(?P<id>[^/]+)/$',
        view=views.queue_detail,
        name='queue_detail'
    ),
    url(
        regex=r'^manage/(?P<id>[^/]+)/$',
        view=views.manage_queue,
        name='manage_queue'
    ),
 
]

