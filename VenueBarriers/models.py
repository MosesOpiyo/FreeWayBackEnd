from django.db import models
from django.db.models.deletion import CASCADE
from FreeWayVenues.models import Venue
# Create your models here.
class VenueBarrier(models.Model):
    Venue = models.ForeignKey(
        Venue,
        on_delete=CASCADE,
        null=True,
        default="",
        related_name="venue"
        )
    Barrier = models.CharField(
        max_length=2,
        blank=True,
        null=True 
    )