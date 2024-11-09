from src.controllers.legal_entity_withdrawer_cash_controller import (
    LegalEntityWithdrawerCashController
    )
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.views.legal_entity_withdrawer_cash_view import LegalEntityWithdrawerCashView

def legal_entity_withdrawer_cash_composer():
    model = LegalEntityRepository(db_connection_handler)
    controller = LegalEntityWithdrawerCashController(model)
    view = LegalEntityWithdrawerCashView(controller)

    return view
