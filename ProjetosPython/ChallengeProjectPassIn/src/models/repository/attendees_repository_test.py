import pytest
from src.models.settings.connection import db_connection_handler
from .attendees_repository import AttendeesRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Se executado, irá gerar novo registro do mesmo usuario, no mesmo evento em nosso banco de dados")
def test_insert_attendee():
    event_id = "event001"
    attendees_info = {
        "uuid": "attendee001",
        "name": "Brunno Manduca",
        "email": "brunnomanducarfe@gmail.com",
        "event_id": event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)
    

@pytest.mark.skip(reason="...")
def test_get_attendee_badge_by_id():
    attendee_id = "attendee001"
    attendees_repository = AttendeesRepository()
    attendee = attendees_repository.get_attendee_badge_by_id(attendee_id)
    
    print(attendee)
    