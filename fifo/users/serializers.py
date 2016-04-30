from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for User
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'name', 'phone', 'email',
                  'groups', 'is_staff', 'is_active', 'is_superuser',
                  'last_login')
        read_only_fields = ('id', 'username', 'email', 'groups', 'is_staff', 'is_active', 'is_superuser',
                  'last_login')
