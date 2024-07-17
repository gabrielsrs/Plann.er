import pytest
import uuid
from .emails_to_invite_repository import EmailsToInviteRepository
from ...models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
email_id = str(uuid.uuid4())

@pytest.mark.skip(reason="db interaction")
def test_repository_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    email_trips_infos = {
        "id": email_id,
        "trip_id": trip_id,
        "email": "rus@mail.com",
    }

    emails_to_invite_repository.repository_email(email_trips_infos)

@pytest.mark.skip(reason="db interaction")
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    email_repository = EmailsToInviteRepository(conn)

    email_repository.find_emails_from_trip(email_id)
