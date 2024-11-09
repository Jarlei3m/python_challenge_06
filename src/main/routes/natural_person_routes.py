from flask import Blueprint, jsonify, request
from src.main.composer.natural_person_checker_statment_composer import (
    natural_person_checker_statment_composer
    )
from src.main.composer.natural_person_deleter_composer import (
    natural_person_deleter_composer
    )
from src.main.composer.natural_person_lister_composer import (
    natural_person_lister_composer
    )
from src.main.composer.natural_person_creator_composer import (
    natural_person_creator_composer
    )
from src.main.composer.natural_person_withdrawer_cash_composer import (
    natural_person_withdrawer_cash_composer
    )
from src.views.http_types.http_request import HttpRequest
from src.errors.error_handler import handle_errors

natural_person_route_bp = Blueprint("natural_person_routes", __name__)

@natural_person_route_bp.route("/natural-person", methods=['GET'])
def list_natural_person():
    try:
        http_request = HttpRequest()
        view = natural_person_lister_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
    
@natural_person_route_bp.route("/natural-person", methods=['POST'])
def create_natural_person():
    try:
        http_request = HttpRequest(body=request.json)
        view = natural_person_creator_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@natural_person_route_bp.route("/natural-person/<nome_completo>", methods=['DELETE'])
def delete_natural_person(nome_completo):
    try:
        http_request = HttpRequest(param={ "nome_completo": nome_completo })
        view = natural_person_deleter_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@natural_person_route_bp.route("/natural-person/withdraw-cash", methods=['PATCH'])
def withdraw_cash_natural_person():
    try:
        http_request = HttpRequest(body=request.json)
        view = natural_person_withdrawer_cash_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@natural_person_route_bp.route(
        "/natural-person/check-statment/<natural_person_id>", methods=['GET']
        )
def check_statment_natural_person(natural_person_id):
    try:
        http_request = HttpRequest(param={ "natural_person_id": natural_person_id})
        view = natural_person_checker_statment_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
