from django.shortcuts import render
from rest_framework.decorators import APIView,api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import GetVenueBarrierSerializer

# Create your views here.
api_view(["GET"])
def all_barriers(request):
    data = {}
    barriers = VenueBarrier.objects.all()
    data = GetVenueBarrierSerializer(barriers,many=True).data
    return Response(data,status = status.HTTP_200_OK)