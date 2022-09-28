from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE, SET_NULL
from django.db import models

from FreeWayVenues.models import Venue
# Create your models here.
class Charges(models.Model):
    venue = models.OneToOneField(
        Venue,
        on_delete=SET_NULL,
        null=True
    )
    charges_amount = models.IntegerField()

    def get_charges(pk):
        """This returns all the events reported regarding a neighbourhood
        Args:
            pk ([type]): [description]
        """
        venue = Venue.objects.get(pk = pk)
        charges = Charges.objects.filter(venue = venue)

        return charges