from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from detourapi.models import DetourUser
from detourapi.serializers.user import UserSerializer


class UserView(ViewSet):
    """Rater games view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
        """
        try:
            user = DetourUser.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except DetourUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        users = DetourUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        detouruser = DetourUser.objects.get(user=request.auth.user)
        currentuser = request.auth.user

        currentuser.first_name = request.data["user"]["first_name"]
        detouruser.phone_number = request.data["phone_number"]
        currentuser.email = request.data["user"]["email"]
        detouruser.allergies = request.data["allergies"]
        detouruser.greenroom_requests = request.data["greenroom_requests"]

        detouruser.save()
        currentuser.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
