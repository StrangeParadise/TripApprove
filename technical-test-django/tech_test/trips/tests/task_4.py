from django.test import TestCase
from django.urls import reverse


class TaskTestCase(TestCase):
    ''' Tests for Task 2 '''

    fixtures = [
        'trips.json',
        'locations.json',
        'destinations.json',
    ]

    def test_task(self):
        response = self.client.get(reverse('trip-list'))
        self.assertEqual(response.status_code, 200)
        expected = [
            {
                "id": 1,
                "name": "Test Trip",
                "destinations": [
                    {
                        "location": "Paris",
                        "start_date": "2021-02-11",
                        "end_date": "2021-02-17"
                    },
                    {
                        "location": "London",
                        "start_date": "2021-02-18",
                        "end_date": "2021-03-23"
                    }
                ]
            },
            {
                "id": 2,
                "name": "Leisure Trip",
                "destinations": [
                    {
                        "location": "Duckburg",
                        "start_date": "2021-01-18",
                        "end_date": "2021-01-23"
                    }
                ]
            },
            {
                "id": 3,
                "name": "Work Trip",
                "destinations": [
                    {
                        "location": "Toronto",
                        "start_date": "2020-12-05",
                        "end_date": "2021-12-30"
                    }
                ]
            }
        ]
        result = response.data
        self.assertEqual(result, expected, 'Failed Task 4 - Trip API did not return expected format')
