from rest_framework import viewsets
from datanyc.models import Cause
from datanyc.serializers import CauseSerializer
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
#@ensure_csrf_cookie
class CauseViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Cause objects """
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer
