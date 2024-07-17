from typing import Dict

class TripConfirmController:
    def __init__(self, trip_repository) -> None:
        self.__trips_repository = trip_repository
        
    def confirm(self, trip_id) -> Dict:
        try:
            self.__trips_repository.update_trip_status(trip_id)

            return {
                "body": None,"status_code": 204
            }

        except Exception as exception:
            return {
                "body": { "error": "Bad request", "message": str(exception) },
                "status_code": 400
            }