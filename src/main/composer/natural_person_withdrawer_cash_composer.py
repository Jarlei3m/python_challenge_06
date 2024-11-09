from src.controllers.natural_person_withdrawer_cash_controller import (
    NaturalPersonWithdrawerCashController
    )
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository
from src.views.natural_person_withdrawer_cash_view import NaturalPersonWithdrawerCashView

def natural_person_withdrawer_cash_composer():
    model = NaturalPersonRepository(db_connection_handler)
    controller = NaturalPersonWithdrawerCashController(model)
    view = NaturalPersonWithdrawerCashView(controller)

    return view
