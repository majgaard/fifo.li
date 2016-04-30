from django.conf.urls import url
from ..users.api_urls import urlpatterns as user_urlpatterns
from ..queues.api_urls import urlpatterns as queue_urlpatterns
from ..entries.api_urls import urlpatterns as entry_urlpatterns

urlpatterns = user_urlpatterns + queue_urlpatterns + entry_urlpatterns