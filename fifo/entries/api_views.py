from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

from .models import Entry
from .serializers import EntrySerializer
from .permissions import IsOwnerOrReadOnly, IsOwner, IsHost

class EntryListView(generics.ListAPIView):

    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    lookup_field = 'id'


class EntryRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    
    permission_classes = (IsAuthenticated, IsOwner)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    lookup_field = 'id'

    
class HostEntryRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    
    permission_classes = (IsAuthenticated, IsHost)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    lookup_field = 'id'
