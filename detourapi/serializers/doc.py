from detourapi.models import Doc
from rest_framework import serializers

class DocSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    
    class Meta:
        model = Doc
        fields = ('id', 'publicURL')
        depth = 1