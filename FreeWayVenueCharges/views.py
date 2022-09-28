from rest_framework.decorators import APIView,api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from rest_framework import status
from rest_framework import generics
from rest_framework.serializers import Serializer

from .serializers import *
from .models import *
from FreeWayVenues.models import Venue

import json
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def charges_view(request,pk):
    data = {}
    
    try:
        venue = Venue.objects.get(pk=pk)
    except :

        data['not found'] = "The neighbourhood was not found"
        return Response(data,status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        charges = Charges.get_charges(pk)
        data = ChargesSerializer(charges,many=False).data

        return Response(data,status= status.HTTP_200_OK)
