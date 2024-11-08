from src.controllers.natural_person_withdrawer_cash_controller import (
    NaturalPersonWithdrawerCashControllerInterface
    )
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class NaturalPersonWithdrawerCashView(ViewInterface):
    def __init__(self, controller: NaturalPersonWithdrawerCashControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        natural_person_info = http_request.body
        body_response = self.__controller.withdraw_cash(natural_person_info)

        return HttpResponse(status_code=200, body=body_response )
    