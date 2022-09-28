from rest_framework import serializers

from .models import *
from FreeWayVenues.serializers import VenueSerializer

class ChargesSerializer(serializers.Serializer):
    venue = VenueSerializer(read_only=True)
    class Meta:
        model = Charges
        fields = '__all__'

    def save(self):
        charges = Charges(charges_amount = self.validated_data['charges_amount'])
        charges.save()
        return charges

