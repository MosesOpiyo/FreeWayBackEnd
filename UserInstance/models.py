from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE, SET_NULL
from django.db import models

from FreeWayAuth.models import Account

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(Account,on_delete=CASCADE,null=True,related_name="profile")
    phone_number = models.IntegerField(unique=True,null=True)

    def __str__(self):
        return self.user.username + "'s " + "profile"

    @receiver(post_save, sender=Account)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=Account)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    
