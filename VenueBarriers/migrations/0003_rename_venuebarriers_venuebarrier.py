# Generated by Django 4.0 on 2022-11-03 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FreeWayVenues', '0005_remove_venue_charging_fees_per_time_and_more'),
        ('VenueBarriers', '0002_alter_venuebarriers_venue'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VenueBarriers',
            new_name='VenueBarrier',
        ),
    ]
