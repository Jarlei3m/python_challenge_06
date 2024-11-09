from src.controllers.natural_person_lister_controller import NaturalPersonListerController
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository
from src.views.natural_person_lister_view import NaturalPersonListerView

def natural_person_lister_composer():
    model = NaturalPersonRepository(db_connection_handler)
    controller = NaturalPersonListerController(model)
    view = NaturalPersonListerView(controller)

    return view
