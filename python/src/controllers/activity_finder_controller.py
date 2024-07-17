from typing import Dict

class ActivityFinderController:
    def __init__(self, activity_repository):
        self.__activity_repository = activity_repository

    def find_from_trip(self, tripId) -> Dict:
        try:
            activities = self.__activity_repository.find_activities_from_trip(tripId)
            
            formatted_activities = []

            for activity in activities:
                formatted_activities.append({
                    "id": activity[0],
                    "title": activity[2],
                    "occurs_at": activity[3],
                })

            return {
                "body": {
                    "activities": formatted_activities
                },"status_code": 200
            }

        except Exception as exception:
            return {
                "body": { "error": "Bad request", "message": str(exception) },
                "status_code": 400
            }