from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from detourapi.models import ScheduleItem, DetourUser
from detourapi.serializers.schedule_item import ScheduleItemSerializer


class ScheduleItemView(ViewSet):
    """Rater games view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
        """
        try:
            scheduleitem = ScheduleItem.objects.get(pk=pk)
            serializer = ScheduleItemSerializer(scheduleitem)
            return Response(serializer.data)
        except ScheduleItem.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        scheduleitems = ScheduleItem.objects.all()
        showDate = request.query_params.get('showDateId', None)
        if showDate is not None:
            scheduleitems = scheduleitems.filter(show_date_id=showDate)
        serializer = ScheduleItemSerializer(scheduleitems, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        user = DetourUser.objects.get(user=request.auth.user)
        if user.user.is_staff != True:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)

        scheduleitem = ScheduleItem.objects.create(
            time=request.data["time"],
            description=request.data["description"],
            show_date=request.data["show_date"],
            user=user
        )
        serializer = ScheduleItemSerializer(scheduleitem)
        return Response(serializer.data)

    def destroy(self, request, pk):
        scheduleitem = ScheduleItem.objects.get(pk=pk)
        user = DetourUser.objects.get(user=request.auth.user)
        if user.user.is_staff != True:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)
        scheduleitem.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)