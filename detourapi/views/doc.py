from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from detourapi.models import DetourUser
from detourapi.models.doc import Doc
from detourapi.serializers.doc import DocSerializer


class DocView(ViewSet):
    """Rater games view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
        """
        try:
            doc = Doc.objects.get(pk=pk)
            serializer = DocSerializer(doc)
            return Response(serializer.data)
        except Doc.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        docs = Doc.objects.all()
        serializer = DocSerializer(docs, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        user = DetourUser.objects.get(user=request.auth.user)
        if user.user.is_staff != True:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)

        doc = Doc.objects.create(
            publicURL=request.data["publicURL"],
            user=user
        )
        serializer = DocSerializer(doc)
        return Response(serializer.data)

