from rest_framework import serializers

from .models import *
from FreeWayAuth.serializers import UserSerializer

class VenueSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Venue
        fields = '__all__'

    def save(self):
        venue = Venue(
            venue_image = self.validated_data['venue_image'],
            name = self.validated_data['name'],
            venue_type = self.validated_data['venue_type'],
            location = self.validated_data['location'],
            parking_spaces = self.validated_data['parking_spaces'],
            time = self.validated_data['time'],
            charging_fees_per_time = self.validated_data['charging_fees_per_time'],
            customer_care_number = self.validated_data['customer_care_number'],
            )
        venue.save()
        return venue 