from email.policy import default
from pyexpat import model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE, SET_NULL
from django.db import models

from FreeWayVenues.models import Venue

# Create your models here.
class Timer(models.Model):
    venue = models.OneToOneField(
        Venue,
        on_delete=CASCADE,
        null=True,
        default="",
        related_name="timer"
    ),
    timerActiveted = models.BooleanField(default=False),
    time = models.TimeField()