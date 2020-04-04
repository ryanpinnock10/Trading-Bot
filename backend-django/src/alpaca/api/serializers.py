from rest_framework import serializers
from ..models import Positions

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = ('__all__')