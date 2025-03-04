from typing import Dict

class ParticipantConfirmController:
    def __init__(self, participant_repository) -> None:
        self.__participant_repository = participant_repository
        
    def confirm(self, participant_id) -> Dict:
        try:
            self.__participant_repository.update_participant_status(participant_id)

            return {
                "body": None,"status_code": 204
            }

        except Exception as exception:
            return {
                "body": { "error": "Bad request", "message": str(exception) },
                "status_code": 400
            }