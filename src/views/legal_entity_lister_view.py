from src.controllers.legal_entity_lister_controller import LegalEntityListerControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class LegalEntityListerView(ViewInterface):
    def __init__(self, controller: LegalEntityListerControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list()

        return HttpResponse(status_code=200, body=body_response )
    