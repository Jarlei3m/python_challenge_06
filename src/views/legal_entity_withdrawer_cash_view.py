from src.controllers.legal_entity_withdrawer_cash_controller import (
    LegalEntityWithdrawerCashControllerInterface
    )
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class LegalEntityWithdrawerCashView(ViewInterface):
    def __init__(self, controller: LegalEntityWithdrawerCashControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        legal_entity_info = http_request.body
        body_response = self.__controller.withdraw_cash(legal_entity_info)

        return HttpResponse(status_code=200, body=body_response )
    