from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

import uuid


@python_2_unicode_compatible
class Queue(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='queues')
    
    name = models.CharField(_('name'), max_length=64, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    
    
    active = models.BooleanField(_('active'), default=False, blank=False)
    
    description = models.TextField(_('queue description'), max_length=512, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('queues:detail', kwargs={'id': self.id})

    
    
    
    
    
    
    
    
    
    
    
