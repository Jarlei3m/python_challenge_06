from src.controllers.legal_entity_deleter_controller import LegalEntityDeleterControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class LegalEntityDeleterView(ViewInterface):
    def __init__(self, controller: LegalEntityDeleterControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        legal_entity_name = http_request.param["nome_fantasia"]
        self.__controller.delete(legal_entity_name)

        return HttpResponse(status_code=204)
    