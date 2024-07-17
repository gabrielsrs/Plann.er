import pytest
import uuid
from .links_repository import LinksRepository
from ...models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())

@pytest.mark.skip(reason="db interaction")
def test_repository_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    email_trips_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "www.inn.com",
        "title": "Inn",
    }

    link_repository.repository_link(email_trips_infos)

@pytest.mark.skip(reason="db interaction")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    response = link_repository.find_links_from_trip(link_id)

    assert isinstance(response, list)
    assert isinstance(response[0], tuple)
