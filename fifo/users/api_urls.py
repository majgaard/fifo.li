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
]
