from typing import Dict
import uuid

class ParticipantCreatorController:
    def __init__(self, emails_repository, participants_repository) -> None:
        self.__emails_repository = emails_repository
        self.__participants_repository = participants_repository

    def create(self, body, trip_id) -> Dict:
        try:
            participant_id = str(uuid.uuid4())
            email_id = str(uuid.uuid4())
            
            email_infos = {
                "email": body["email"],
                "trip_id": trip_id,
                "id": email_id,
                
            }

            participant_infos = {
                "id": participant_id,
                "trip_id": trip_id,
                "emails_to_invite_id": email_id,
                "name": body["name"],
                
            }

            self.__emails_repository.repository_email(email_infos)
            self.__participants_repository.registry_participant(participant_infos)

            return {
                "body": { "participant_id": participant_id },
                "status_code": 201
            }
        
        except Exception as exception:
            return {
                "body": { "error": "Bad request", "message": str(exception) },
                "status_code": 400
            }
