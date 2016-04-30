from django.conf.urls import url
from . import api_views


urlpatterns = [
    #	{% url "api_v1:users" %}
    url(
            regex=r'users/$',
            view=api_views.UserListView.as_view(),
            name='users'
    ),
    url(
            regex=r'users/(?P<id>[\w.@+-]+)/$',
            view=api_views.UserRetrieveUpdateView.as_view(),
            name='user'
    ),
    url(
            regex=r'users/exists/orgid/(?P<org_id>\d+)/$',
            view=api_views.UserRetrieveViewOrgId.as_view(),
            name='user_exists_orgid'
    ),
    url(
            regex=r'users/exists/id/(?P<id>\d+)/$',
            view=api_views.UserRetrieveViewId.as_view(),
            name='user_exists_id'
    ),
    
]
