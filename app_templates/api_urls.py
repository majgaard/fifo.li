from django.conf.urls import url
from . import api_views


urlpatterns = [
    #	{% url "api:view_name_unique" %}
    url(
            regex=r'app_name/$',
            view=api_views.view_name.as_view(),
            name='view_name_unique'
    ),
]
