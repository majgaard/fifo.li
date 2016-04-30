from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

from .models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly, IsOwner


class UserListView(generics.ListAPIView):

    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UserRetrieveViewOrgId(generics.RetrieveAPIView):

    #permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'org_id'

class UserRetrieveViewId(generics.RetrieveAPIView):

    #permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    
    permission_classes = (IsAuthenticated, IsOwner)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    
    
