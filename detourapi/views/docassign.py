from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from detourapi.models import DetourUser
from detourapi.models.doc_assignment import DocAssignment
from detourapi.models.show_date import ShowDate
from detourapi.models.doc import Doc
from detourapi.serializers.docassignment import DocAssignmentSerializer


class DocAssignView(ViewSet):

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        user = DetourUser.objects.get(user=request.auth.user)
        if user.user.is_staff != True:
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)

        doc = Doc.objects.get(pk=request.data["docId"])
        show_date = ShowDate.objects.get(pk=request.data["showDateId"])

        doc = DocAssignment.objects.create(
            doc=doc,
            show_date=show_date
        )
        serializer = DocAssignmentSerializer(doc)
        return Response(serializer.data)