from detourapi.models import Status
from rest_framework import serializers

class StatusSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    
    class Meta:
        model = Status
        fields = ('id', 'status')
        depth = 1