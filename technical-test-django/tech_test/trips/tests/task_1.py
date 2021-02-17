import os
import sys

from django.core.management import call_command
from django.test import TestCase

from trips.models import Trip


class TaskTestCase(TestCase):
    ''' Tests for Task 1 '''
    fixtures = [
        'trips.json',
    ]

    def setUp(self):
        self.trip = Trip.objects.get(name='Test Trip')

    def test_task(self):
        try:
            from trips.models import Location
        except Exception:
            raise Exception('Failed Task 1.a. - There is no Location model')

        call_command('loaddata', 'locations.json')
        self.assertTrue(
            hasattr(self.trip, 'locations'),
            'Failed Task 1.b. - Trip has no locations'
        )

        self.assertEqual(
            self.trip.locations.count(), 0,
            'Failed Task 1.b. - Trip should be able to have no location'
        )

        # check locations are mapped
        call_command('loaddata', 'triplocations.json')
        self.assertEqual(
            self.trip.locations.count(), 2,
            'Failed Task 1.b. - Trip should be able to have more than one location'
        )

        # check locations have many trips
        location = self.trip.locations.first()
        self.assertTrue(
            hasattr(location, 'trip_set'),
            'Failed Task 1.b. - Locations should have zero or more trips'
        )
