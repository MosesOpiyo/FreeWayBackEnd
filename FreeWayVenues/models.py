from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE, SET_NULL
from django.db import models

from UserInstance import models as profile

# Create your models here.
class Venue(models.Model):
    venue_image = CloudinaryField(null=True)
    name = models.CharField(
        max_length=500,
        unique=True,
        blank=True,
        null=True,
    )
    venue_type = models.CharField(
        max_length=500,
        unique=True,
        blank=True,
        null=True
    )
    location = models.CharField(
        max_length=500,
        blank=True,
        null=True 
    )
    parking_spaces = models.IntegerField()
    customer_care_number = models.IntegerField(null=True)

    def __str__(self):
      return self.name

    def single_venue(pk):
        """This returns single venue
        Args:
            pk ([type]): [description]
        """
        venue = Venue.objects.get(pk = pk)

        return venue