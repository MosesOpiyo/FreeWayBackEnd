# Generated by Django 4.1 on 2022-09-03 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FreeWayVenues', '0004_venue_customer_care_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='charging_fees_per_time',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='time',
        ),
    ]