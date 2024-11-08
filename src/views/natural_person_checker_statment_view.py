from src.controllers.natural_person_checker_statment_controller import (
    NaturalPersonCheckerStatmentControllerInterface
    )
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class NaturalPersonCheckerStatmentView(ViewInterface):
    def __init__(self, controller: NaturalPersonCheckerStatmentControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        natural_person_id = http_request.param["id"]
        body_response = self.__controller.check_statment(natural_person_id)

        return HttpResponse(status_code=200, body=body_response )
    