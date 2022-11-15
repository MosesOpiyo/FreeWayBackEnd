from rest_framework import serializers
from models import Timer

class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = ['timerActivated']

    def save(self):
        time = Timer(time=self.validated_data['timerActivated'])
        time.save()
        return time