from detourapi.models import DocAssignment
from rest_framework import serializers

class DocAssignmentSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    
    class Meta:
        model = DocAssignment
        fields = ('id', 'doc_id', 'show_date_id')
        depth = 1