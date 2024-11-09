from flask import Blueprint, jsonify, request
from src.main.composer.legal_entity_checker_statment_composer import (
    legal_entity_checker_statment_composer
    )
from src.main.composer.legal_entity_creator_composer import (
    legal_entity_creator_composer
    )
from src.main.composer.legal_entity_deleter_composer import (
    legal_entity_deleter_composer
    )
from src.main.composer.legal_entity_lister_composer import (
    legal_entity_lister_composer
    )
from src.main.composer.legal_entity_withdrawer_cash_composer import (
    legal_entity_withdrawer_cash_composer
    )
from src.views.http_types.http_request import HttpRequest

legal_entity_route_bp = Blueprint("legal_entity_routes", __name__)

@legal_entity_route_bp.route("/legal-entity", methods=['GET'])
def list_legal_entity():
    http_request = HttpRequest()
    view = legal_entity_lister_composer()

    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@legal_entity_route_bp.route("/legal-entity", methods=['POST'])
def create_legal_entity():
    http_request = HttpRequest(body=request.json)
    view = legal_entity_creator_composer()

    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@legal_entity_route_bp.route("/legal-entity/<nome_fantasia>", methods=['DELETE'])
def delete_legal_entity(nome_fantasia):
    http_request = HttpRequest(param={ "nome_fantasia": nome_fantasia })
    view = legal_entity_deleter_composer()

    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@legal_entity_route_bp.route("/legal-entity/withdraw-cash", methods=['PATCH'])
def withdraw_cash_legal_entity():
    http_request = HttpRequest(body=request.json)
    view = legal_entity_withdrawer_cash_composer()

    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@legal_entity_route_bp.route(
        "/legal-entity/check-statment/<legal_entity_id>", methods=['GET']
        )
def check_statment_legal_entity(legal_entity_id):
    http_request = HttpRequest(param={ "legal_entity_id": legal_entity_id})
    view = legal_entity_checker_statment_composer()

    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code
