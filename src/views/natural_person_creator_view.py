from src.controllers.natural_person_creator_controller import (
    NaturalPersonCreatorControllerInterface
    )
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class NaturalPersonCreatorView(ViewInterface):
    def __init__(self, controller: NaturalPersonCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        natural_person_info = http_request.body
        body_response = self.__controller.create(natural_person_info)

        return HttpResponse(status_code=201, body=body_response )
    