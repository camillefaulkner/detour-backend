from detourapi.models import ScheduleItem
from rest_framework import serializers

class ScheduleItemSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    
    class Meta:
        model = ScheduleItem
        fields = ('id', 'time', 'description', 'show_date_id')
        depth = 1