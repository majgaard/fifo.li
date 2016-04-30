from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

from .models import Queue
from .serializers import QueueSerializer
from .permissions import IsOwnerOrReadOnly, IsOwner


class QueueListView(generics.ListAPIView):

    queryset = Queue.objects.filter(active=True)
    serializer_class = QueueSerializer
    lookup_field = 'id'

class HostQueueListView(generics.ListAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = QueueSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        return Queue.objects.filter(owner=self.request.user)
    
class StaffQueueListView(generics.ListAPIView):
    
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer
    lookup_field = 'id'


class QueueRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = (IsAuthenticated, IsOwner)
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer
    lookup_field = 'id'
    
    
class StaffQueueRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer
    lookup_field = 'id'
    

class QueueRetrieveView(generics.RetrieveAPIView):
    queryset = Queue.objects.filter(active=True)
    serializer_class = QueueSerializer
    lookup_field = 'id'
    