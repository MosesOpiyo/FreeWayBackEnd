from rest_framework import serializers

from .models import License_Plate, Phone_Number, Profile
from FreeWayAuth.serializers import UserSerializer

class PhoneNumberSerializer(serializers.Serializer):
    class Meta:
        model = Phone_Number
        fields = '__all__'
    
    def save(self,request):
        phoneNumber = Phone_Number(
            phoneNumber=self.validated_data['phoneNumber'],
            )
        phoneNumber.save()
        return phoneNumber 

class GetPhoneNumberSerializer(serializers.ModelSerializer):
    """This deals with parsing the phone number model
    Args:
        serializers ([type]): [description]
    """
    class Meta:
        model = Phone_Number
        fields = '__all__'

class LicensePlateSerializer(serializers.Serializer):
    class Meta:
        model = License_Plate
        fields = '__all__'
    
    def save(self,request):
        licensePlate = License_Plate(
            licensePlate=self.validated_data['licensePlate']
            )
        licensePlate.save()
        return licensePlate 

class GetLicensePlateSerializer(serializers.ModelSerializer):
    """This deals with parsing the license model
    Args:
        serializers ([type]): [description]
    """
    class Meta:
        model = License_Plate
        fields = '__all__'


class ProfileSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    phoneNumber = GetPhoneNumberSerializer(read_only=True)
    licensePlate = GetLicensePlateSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'


