from detourapi.models import GreenRoomRequest
from rest_framework import serializers

class GreenRoomSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    
    class Meta:
        model = GreenRoomRequest
        fields = ('id', 'request', 'show_date', 'status', 'user')
        depth = 1