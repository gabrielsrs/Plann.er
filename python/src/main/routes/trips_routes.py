from flask import jsonify, Blueprint, request

trip_routes_bp = Blueprint("trip_routes", __name__)

# Controllers Imports
from src.controllers.trip_creator_controller import TripCreatorController
from src.controllers.trip_finder_controller import TripFinderController
from src.controllers.trip_confirm_controller import TripConfirmController
from src.controllers.link_creator_controller import LinkCreatorController
from src.controllers.link_finder_controller import LinkFinderController
from src.controllers.activity_creator_controller import ActivityCreatorController
from src.controllers.participant_creator_controller import ParticipantCreatorController
from src.controllers.activity_finder_controller import ActivityFinderController
from src.controllers.participant_finder_controller import ParticipantFinderController
from src.controllers.participant_confirm_controller import ParticipantConfirmController

# Repositories Imports
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.repositories.participants_repository import ParticipantsRepository

# Connection Handler Import
from src.models.settings.db_connection_handler import db_connection_handler

@trip_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = TripCreatorController(trips_repository, emails_repository)

    response = controller.create(request.json)

    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trips(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFinderController(trips_repository)

    response = controller.find_trip_details(tripId)

    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def create_confirm_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripConfirmController(trips_repository)

    response = controller.confirm(tripId)

    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkCreatorController(links_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_links(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkFinderController(links_repository)

    response = controller.find(tripId)

    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity(tripId):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    controller = ActivityCreatorController(activities_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def invite_to_trip(tripId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = ParticipantCreatorController(emails_repository, participants_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def get_trip_activities(tripId):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    controller = ActivityFinderController(activities_repository)

    response = controller.find_from_trip(tripId)

    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])
def get_trip_participants(tripId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantFinderController(participants_repository)

    response = controller.find_participants_from_trip(tripId)

    return jsonify(response["body"]), response["status_code"]

@trip_routes_bp.route("/participants/<participantId>/confirm", methods=["PATCH"])
def confirm_participant(participantId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantConfirmController(participants_repository)

    response = controller.confirm(participantId)

    return jsonify(response["body"]), response["status_code"]
