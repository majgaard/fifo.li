from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

from .models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly, IsOwner


