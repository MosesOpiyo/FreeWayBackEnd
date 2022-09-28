from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import ProfileSerializer
from .models import Profile

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):

    data = {}
    print(request.user)
    profile = Profile.objects.get(user = request.user)
    data =  ProfileSerializer(profile).data
    print(data)
    return Response(data,status = status.HTTP_200_OK)