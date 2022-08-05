from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from detourapi.models import ShowDate, DetourUser
from detourapi.serializers.show_date import ShowDateSerializer


class ShowDateView(ViewSet):
    """Rater games view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
        """
        try:
            showdate = ShowDate.objects.get(pk=pk)
            serializer = ShowDateSerializer(showdate)
            return Response(serializer.data)
        except ShowDate.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        showdates = ShowDate.objects.all()
        serializer = ShowDateSerializer(showdates, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        user = DetourUser.objects.get(user=request.auth.user)
        if user.user.is_staff != True:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)

        showdate = ShowDate.objects.create(
            date=request.data["date"],
            venue=request.data["venue"],
            street_address=request.data["street_address"],
            city=request.data["city"],
            state=request.data["state"],
            essential_notes=request.data["essential_notes"],
            other=request.data["other"],
            user=user
        )
        serializer = ShowDateSerializer(showdate)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        user = DetourUser.objects.get(user=request.auth.user)

        showdate = ShowDate.objects.get(pk=pk)
        if user.id != showdate.user_id:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)
        showdate.date = request.data["date"]
        showdate.venue = request.data["venue"]
        showdate.street_address = request.data["street_address"]
        showdate.city = request.data["city"]
        showdate.state = request.data["state"]
        showdate.essential_notes = request.data["essential_notes"]
        showdate.other = request.data["other"]

        showdate.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        showdate = ShowDate.objects.get(pk=pk)
        user = DetourUser.objects.get(user=request.auth.user)
        if user.id != showdate.user_id:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)
        showdate.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
