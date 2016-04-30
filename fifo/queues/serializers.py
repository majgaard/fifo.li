from rest_framework import serializers


from .models import Queue

class QueueSerializer(serializers.ModelSerializer):
    """
    Serializer class for Queue
    """

    class Meta:
        model = Queue
        fields = ('id', 'active', 'name', 'owner', 'description', 'created',)
        read_only_fields = ('id', 'owner', 'created',)
