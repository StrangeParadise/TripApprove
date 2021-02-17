from django.db import models

class Location(models.Model):
    ''' Location model '''

    name = models.CharField(max_length=256)

class Trip(models.Model):
    ''' Trip model '''

    STATUS = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('DECLINED', 'Declined'),
        ('CANCELLED', 'Cancelled'),
    ]
    status = models.CharField(
        default='PENDING',
        choices=STATUS,
        max_length=10,
    )
    created = models.DateField(auto_now=True)
    name = models.CharField(max_length=256)
    locations = models.ManyToManyField(Location)

class Destination(models.Model):
    ''' Destination model '''

    start_date = models.DateField()
    end_date = models.DateField()
    location = models.OneToOneField(Location, on_delete=models.CASCADE, default=1)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, default=1)
