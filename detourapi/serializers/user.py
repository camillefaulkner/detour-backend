from detourapi.models.detour_user import DetourUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    
    class Meta:
        model = DetourUser
        fields = ('id', 'phone_number', 'allergies', 'greenroom_requests', 'user', 'full_name')
        depth = 1