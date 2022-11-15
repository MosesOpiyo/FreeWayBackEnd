from rest_framework import serializers

from .models import *
from FreeWayAuth.serializers import UserSerializer

class VenueBarriersSerializer(serializers.Serializer):
    class Meta:
        model = VenueBarrier
        fields = '__all__'

    def save(self):
        barrier = VenueBarrier(
            Barrier = self.validated_data['Barrier'],
            
            )
        barrier.save()
        return barrier

class GetVenueBarrierSerializer(serializers.ModelSerializer):
    """This deals with parsing the profile model
    Args:
        serializers ([type]): [description]
    """
   
    class Meta:
        model = VenueBarrier
        fields = '__all__'