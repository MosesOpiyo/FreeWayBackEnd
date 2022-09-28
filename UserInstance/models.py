from email.policy import default
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE, SET_NULL
from django.db import models



from FreeWayAuth.models import Account

# Create your models here.
class Phone_Number(models.Model):
    phone_number = models.IntegerField(
    unique=True,
    null=True,
    blank=True
    )
    def __str__(self):
        return  f"{self.phone_number}"

class License_Plate(models.Model):
    license_plate = models.CharField(
    max_length=10,
    null=True,
    unique=True,
    blank=True
    )
    def __str__(self):
        return  f"{self.license_plate}"

class Profile(models.Model):
    user = models.OneToOneField(
    Account,
    on_delete=CASCADE,
    null=True,
    default="",
    related_name="profile"
    )
    phoneNumber = models.OneToOneField(
        Phone_Number,
        on_delete=CASCADE,
        null = True,
        default="",
        related_name="number"
    )

    licensePlate = models.OneToOneField(
        License_Plate,
        on_delete=CASCADE,
        null=True,
        default="",
        related_name="plate"
    )

    def __str__(self):
        return  f"{self.user.username}'s profile"

    @receiver(post_save, sender=Account)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=Account)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    
