from detourapi.models import ShowDate
from rest_framework import serializers

class ShowDateSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    
    class Meta:
        model = ShowDate
        fields = ('id', 'date', 'venue', 'street_address', 'city', 'state','essential_notes', 'other', 'user_id', 'schedule_items', 'guest_requests', 'gr_requests', 'docs')
        depth = 2