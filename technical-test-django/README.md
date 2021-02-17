## Setup

Make sure that you have Python 3.8 installed

Make sure that you have pipenv installed
```
pip install pipenv --dev
```

Move to the director and create a pipenv project
```
pipenv install
```

Check your installation by running
```
pipenv shell
python --version
python -m django --version
```

It should return
```
Python 3.8.0
Django 3.0.11
```

## Tasks

### Task 1. Add locations

At the moment, we only have a single model, a `Trip`.
We want to create a new model to represent locations where a trip planned for.

**1.a. Location model**

In `/tech_test/trips/models.py` create a new model for `Location` objects. with the following field:
  - name    (char field)  

**1.b. Trip-Location relationship**

In the `Trip` model, add a field `locations` representing the `Trip` - `Location` relationship, with the following requirements:
- A Trip may have zero or more Locations.
- A Location may belong to zero or more Trips.


To test that this task is successful, run `./tech_test/manage.py test trips.tests.task_1`


### Task 2. Update the Destination model

We now want to record information about how long a user has spent in a location during their Trip.

**2.a. Destination model**

Add a `Destination` model which represents how long a `Trip` lasts in a specific `Location`, with the following fields:
- start_date  (date)
- end_date    (date)
- location    (Location)
- trip        (Trip)

**2.b. Destination relationship**

For simplicity, update the `Destination.trip` field so that the following works:
```
trip = Trip.objects.first()
trip.destinations.all()
```


To test that this task is successful, run `./tech_test/manage.py test trips.tests.task_2`


### Task 3. Migrating old data

The issue with our previous request, is that our application has been in production for a while.
Users have been creating trips and locations in our system.

Before deploying our latest addition, we need to write a migration to migrate user data
from: Trip - Location
to:   Trip - Destination - Location

Write a migration file to handle this.


### Task 4. API View

We need to build an API so that our frontend code can retrieve the list of trips created.

In the file `./tech_test/trips/views.py`, make the necessary updates so that the view works.

Use the official Django REST Framework documentations available at https://www.django-rest-framework.org/

The end results should be an API which returns at the following URL: `http://localhost:8000/api/trips/`
all the trips available in the format:
```
  [
      {
          "id": <trip.id>,
          "name": "<trip.name>",
          "destinations": [
              {
                  "location": "<trip.destinations[0].location.name>",
                  "start_date": "<trip.destinations[0].start_date>",
                  "end_date": "<trip.destinations[0].end_date>"
              },
              [...]
          ]
      },
      [...]
  ]
```

To test that this task is successful, run `./tech_test/manage.py test trips.tests.task_4`
