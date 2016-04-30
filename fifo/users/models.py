# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

import uuid


@python_2_unicode_compatible
class User(AbstractUser):
    
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    org_id = models.IntegerField(_('Organization ID'), blank=False)
    name = models.CharField(_('Name of User'), blank=False, max_length=255)
    
    phone = models.CharField(_('Phone Number'), max_length=10, blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
