from src.controllers.legal_entity_deleter_controller import LegalEntityDeleterController
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.views.legal_entity_deleter_view import LegalEntityDeleterView

def legal_entity_deleter_composer():
    model = LegalEntityRepository(db_connection_handler)
    controller = LegalEntityDeleterController(model)
    view = LegalEntityDeleterView(controller)

    return view
