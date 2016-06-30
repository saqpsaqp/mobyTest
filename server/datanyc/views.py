from rest_framework import viewsets
from datanyc.models import Cause
from datanyc.serializers import CauseSerializer

# Create your views here.
class CauseViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Cause objects """
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer
