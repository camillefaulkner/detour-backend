from detourapi.models import GuestRequest
from rest_framework import serializers
from .user import UserSerializer

class GuestRequestSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    user = UserSerializer()

    class Meta:
        model = GuestRequest
        fields = ('id', 'name', 'quantity', 'show_date', 'status', 'user')
        depth = 1

