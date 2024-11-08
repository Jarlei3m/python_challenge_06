from src.controllers.natural_person_deleter_controller import (
    NaturalPersonDeleterControllerInterface
    )
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class NaturalPersonDeleterView(ViewInterface):
    def __init__(self, controller: NaturalPersonDeleterControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        natural_person_name = http_request.param["nome_completo"]
        self.__controller.delete(natural_person_name)

        return HttpResponse(status_code=204)
    