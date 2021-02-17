from django.core.management import call_command
from django.test import TestCase

from trips.models import Trip


class TaskTestCase(TestCase):
    ''' Tests for Task 2 '''

    fixtures = [
        'trips.json',
        'locations.json',
    ]

    def test_task(self):
        try:
            from trips.models import Destination
        except Exception:
            raise Exception('Failed Task 2.a - There is no Destination model')

        self.assertTrue(
            hasattr(Destination, 'start_date'),
            'Failed Task 2.a - Destination has no start_date'
        )
        self.assertTrue(
            hasattr(Destination, 'end_date'),
            'Failed Task 2.a - Destination has no end_date'
        )
        self.assertTrue(
            hasattr(Destination, 'trip'),
            'Failed Task 2.a - Destination has no trip'
        )
        self.assertTrue(
            hasattr(Destination, 'location'),
            'Failed Task 2.a - Destination has no location'
        )

        trip = Trip.objects.first()
        self.assertTrue(
            hasattr(trip, 'destinations'),
            'Failed Task 2.b - Destination has no location'
        )
