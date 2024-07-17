from typing import Dict
import uuid

class ActivityCreatorController:
    def __init__(self, activity_repository) -> None:
        self.__activity_repository = activity_repository

    def create(self, body, trip_id) -> Dict:
        try:
            activity_id = str(uuid.uuid4())
            
            activity_infos = {
                "id": activity_id,
                "trip_id": trip_id,
                "title": body["title"],
                "occurs_at": body["occurs_at"],
                
            }

            self.__activity_repository.repository_activities(activity_infos)

            return {
                "body": { "activity_id": activity_id },
                "status_code": 201
            }
        
        except Exception as exception:
            return {
                "body": { "error": "Bad request", "message": str(exception) },
                "status_code": 400
            }
