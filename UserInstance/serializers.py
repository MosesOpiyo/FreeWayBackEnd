from rest_framework import serializers

from .models import Profile
from FreeWayAuth.serializers import UserSerializer

class ProfileSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['phone_number','license_plate']

    def save(self,request):
        profile = Profile(
            user = request.user,
            phone_number=self.validated_data['phone_number'],
            license_plate=self.validated_data['license_plate']
            )
        profile.save()
        return profile 