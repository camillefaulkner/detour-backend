from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from detourapi.models import GreenRoomRequest, DetourUser
from detourapi.models.show_date import ShowDate
from detourapi.models.status import Status
from detourapi.serializers.greenroom_request import GreenRoomSerializer


class GreenRoomRequestView(ViewSet):
    """Rater games view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
        """
        try:
            greenroom = GreenRoomRequest.objects.get(pk=pk)
            serializer = GreenRoomSerializer(greenroom)
            return Response(serializer.data)
        except GreenRoomRequest.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        greenrooms = GreenRoomRequest.objects.all()
        showDate = request.query_params.get('showDateId', None)
        if showDate is not None:
            greenrooms = greenrooms.filter(show_date_id=showDate)
        status = request.query_params.get('statusId', None)
        if status is not None:
            greenrooms = greenrooms.filter(status_id=status)
        user = DetourUser.objects.get(user=request.auth.user)
        if user is not None:
            greenrooms = greenrooms.filter(user_id=user)
        serializer = GreenRoomSerializer(greenrooms, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        status = Status.objects.get(pk=request.data["statusId"])
        show_date = ShowDate.objects.get(pk=request.data["showDateId"])
        user = DetourUser.objects.get(user=request.auth.user)
        if user.user.is_staff == True:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)

        greenroom = GreenRoomRequest.objects.create(
            request=request.data["request"],
            show_date=show_date,
            status=status,
            user=user
        )
        serializer = GreenRoomSerializer(greenroom)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        user = DetourUser.objects.get(user=request.auth.user)
        if user.user.is_staff != True:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)

        greenroom = GreenRoomRequest.objects.get(pk=pk)
        greenroom.status = request.data["status"]

        greenroom.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
