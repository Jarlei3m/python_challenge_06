from src.controllers.legal_entity_creator_controller import LegalEntityCreatorController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class LegalEntityView(ViewInterface):
    def __init__(self, controller: LegalEntityCreatorController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        legal_entity_info = http_request.body
        body_response = self.__controller.create(legal_entity_info)

        return HttpResponse(status_code=201, body=body_response )
    