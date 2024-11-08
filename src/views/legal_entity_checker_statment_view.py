from src.controllers.legal_entity_checker_statment_controller import (
    LegalEntityCheckerStatmentControllerInterface
    )
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class LegalEntityCheckerStatmentView(ViewInterface):
    def __init__(self, controller: LegalEntityCheckerStatmentControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        legal_entity_id = http_request.param["id"]
        body_response = self.__controller.check_statment(legal_entity_id)

        return HttpResponse(status_code=200, body=body_response )
    