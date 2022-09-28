from rest_framework import serializers

from .models import *
from FreeWayAuth.serializers import UserSerializer

class VenueSerializer(serializers.Serializer):
    class Meta:
        model = Venue
        fields = '__all__'

    def save(self):
        venue = Venue(
            venueimage = self.validated_data['venue_image'],
            name = self.validated_data['name'],
            venuetype = self.validated_data['venue_type'],
            location = self.validated_data['location'],
            parkingspaces = self.validated_data['parking_spaces'],
            customercare = self.validated_data['customer_care_number'],
            )
        venue.save()
        return venue 

class GetVenueSerializer(serializers.ModelSerializer):
    """This deals with parsing the profile model
    Args:
        serializers ([type]): [description]
    """
   
    class Meta:
        model = Venue
        fields = '__all__'