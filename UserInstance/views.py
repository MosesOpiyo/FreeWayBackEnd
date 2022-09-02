from cProfile import Profile
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProfileSerializer

# Create your views here.
@api_view(['GET'])   
def user_profile(request):
    data = {}
    profile = Profile.objects.get(user = request.user)
    print(profile.user.username)
    data =  ProfileSerializer(profile).data
    return Response(data,status = status.HTTP_200_OK)