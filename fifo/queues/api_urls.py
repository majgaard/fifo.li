from django.conf.urls import url
from . import api_views


urlpatterns = [
    #	{% url "api_v1:queues" %}
    url(
            regex=r'queues/$',
            view=api_views.QueueListView.as_view(),
            name='queues'
    ),
    url(
            regex=r'queues/(?P<id>[\w.@+-]+)/$',
            view=api_views.QueueRetrieveUpdateDestroyView.as_view(),
            name='queue'
    ),
    
    url(
            regex=r'staff/queues/$',
            view=api_views.StaffQueueListView.as_view(),
            name='staff_queues'
    ),
    url(
            regex=r'host/queues/$',
            view=api_views.HostQueueListView.as_view(),
            name='host_queues'
    ),
  
    url(
            regex=r'staff/queues/(?P<id>[\w.@+-]+)/$',
            view=api_views.StaffQueueRetrieveUpdateDestroyView.as_view(),
            name='staff_queue'
    ),
]
