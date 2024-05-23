import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

# @pytest.mark.skip(reason="Se executado, irá gerar novo registro no banco de dados")
def test_insert_event():
    event = {
        "uuid": "event004",
        "title": "title event 004",
        "slug": "slug event 004",
        "maximum_attendees": 45
    }
    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)


@pytest.mark.skip(reason="Ação somente para retornar informações de um event")
def test_get_event_by_id():
    event_id = "event010"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)
    