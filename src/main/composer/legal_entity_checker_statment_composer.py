from src.controllers.legal_entity_checker_statment_controller import (
    LegalEntityCheckerStatmentController
    )
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.views.legal_entity_checker_statment_view import LegalEntityCheckerStatmentView

def legal_entity_checker_statment_composer():
    model = LegalEntityRepository(db_connection_handler)
    controller = LegalEntityCheckerStatmentController(model)
    view = LegalEntityCheckerStatmentView(controller)

    return view
