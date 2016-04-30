from django.conf.urls import url
from . import api_views


urlpatterns = [
    #	{% url "api:entries" %}
    url(
            regex=r'entries/$',
            view=api_views.EntryListView.as_view(),
            name='entries'
    ),
    url(
            regex=r'entries/(?P<id>[\w.@+-]+)/$',
            view=api_views.EntryRetrieveUpdateView.as_view(),
            name='entry'
    ),
    url(
            regex=r'host/entries/(?P<id>[\w.@+-]+)/$',
            view=api_views.HostEntryRetrieveUpdateView.as_view(),
            name='host_entry'
    ),
]

