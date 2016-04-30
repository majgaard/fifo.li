from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from ..queues.models import Queue

import uuid

@python_2_unicode_compatible
class Entry(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='entries')
    queue = models.ForeignKey(Queue, null=False, related_name='entries')
    created = models.DateTimeField(auto_now_add=True)
    
    start = models.DateTimeField(_('start date'), blank=True, null=True)
    finish = models.DateTimeField(_('finish date'), blank=True, null=True)
    
    
    resolved = models.BooleanField(_('resolved'), default=False, blank=False)
    active = models.BooleanField(_('active'), default=True, blank=False)

    #description = models.TextField(_('entry description'), max_length=512, blank=True)

    def __str__(self):
        return self.owner.name + " Entry"

    def get_absolute_url(self):
        return reverse('entries:detail', kwargs={'id': self.id})

    
    
    
    