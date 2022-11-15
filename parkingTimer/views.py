from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import time

from .serializers import *

def activateTimer(request):
    serializer = TimerSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        timer = serializer.save()
        data['response'] = f"Timer activation has been set to {timer.timerActivated}"
        return Response(data,status = status.HTTP_200_OK)
    else:
        data = serializer.errors
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

def parkingTimer():
    while Timer.timerActivated == True:
        try:
            start_time = time.time()
            print("Timer has started.")
        except Timer.timerActivated == False:
            end_time = time.time()
            time_spent = round(end_time - start_time,0)
            data = {}

            charged_time = time_spent - 1800
            if(charged_time > 0):
                charge_rates = round(50 % 1800,2)
                charge = charged_time * charge_rates 
                if(charge <= 0):
                    data["response"] = f"Your time is{time}"
                    return Response(data,status = status.HTTP_200_OK)
                elif(charge > 0):
                    data["response"] = f"Your time is {time} with placed charge of {charge}"


    



