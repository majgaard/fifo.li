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
            regex=r'entries/create/$',
            view=api_views.EntryCreateView.as_view(),
            name='create_entry'
    ),
    url(
            regex=r'entries/active/(?P<owner>[\w.@+-]+)/$',
            view=api_views.ActiveEntryRetrieveView.as_view(),
            name='active_entry'
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

