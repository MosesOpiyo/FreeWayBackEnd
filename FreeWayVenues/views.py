from rest_framework.decorators import APIView,api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from rest_framework import status
from rest_framework import generics
from rest_framework.serializers import Serializer

from .serializers import *
from .models import *

import json
# Create your views here.
@api_view(['GET'])
def venue_view(request):
    data = {}

    if request.method == 'GET':
        venues = Venue.objects.all()
        data = GetVenueSerializer(venues,many=True).data
        return Response(data,status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def singleVenue(request,pk):
    data = {}

    if request.method == 'GET':
        venue = Venue.single_venue(pk)
        data = GetVenueSerializer(venue).data
        return Response(data,status = status.HTTP_200_OK)