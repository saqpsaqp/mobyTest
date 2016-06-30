from rest_framework import serializers
from datanyc.models import Cause

class CauseSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Cause model """
    class Meta:
        model = Cause
        fields = ("id","year", "ethnicity", "sex", "cause", "count", "percent")

