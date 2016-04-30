from rest_framework import serializers

from .models import Entry

class EntrySerializer(serializers.ModelSerializer):
    """
    Serializer class for Entry
    """
    
    class Meta:
        model = Entry
        fields = ('id', 'active', 'queue', 'owner', 'created', 'start', 'finish', 'resolved',)
        read_only_fields = ('id', 'owner', 'queue', 'created',)