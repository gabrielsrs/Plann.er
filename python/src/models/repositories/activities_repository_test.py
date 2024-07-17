from datetime import datetime
import uuid
import pytest
from .activities_repository import ActivitiesRepository
from ...models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
activity_id = str(uuid.uuid4())

@pytest.mark.skip(reason="db interaction")
def test_repository_activities():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activity_infos = {
        "id": activity_id,
        "trip_id": trip_id,
        "title": "Ride Bike",
        "occurs_at": datetime.strptime("14-11-2024", "%d-%m-%Y"),
    }

    activities_repository.repository_activities(activity_infos)

@pytest.mark.skip(reason="db interaction")
def test_find_activities_from_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activities_repository.find_activities_from_trip(trip_id)
