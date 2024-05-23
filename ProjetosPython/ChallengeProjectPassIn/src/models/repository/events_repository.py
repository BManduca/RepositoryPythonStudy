from typing import Dict
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events


class EventsRepository:
    def insert_event(self, events_info: Dict) -> Dict:
        # entrando no contexto (criando a seção)
        with db_connection_handler as database:
            try:
                event = Events(
                    id = events_info.get("uuid"),
                    title = events_info.get("title"),
                    details = events_info.get("details"),
                    slug = events_info.get("slug"),
                    maximum_attendees = events_info.get("maximum_attendees")
                )
                database.session.add(event)
                database.session.commit()
            
                return events_info
            
            except IntegrityError:
                raise Exception("Este evento já foi cadastrado!")
                
            # caso aconteça um erro, efetuamos um rollback, para cuidar do DB
            except Exception as exception:
                database.session.rollback()
                raise exception
        
        
    def get_event_by_id(self, event_id: str) -> Events:
        with db_connection_handler as database:
            try:
                event = (
                    database.session
                        .query(Events)    
                        .filter(Events.id == event_id)
                        .one()
                )
                return event
            except NoResultFound:
                return None
        
        