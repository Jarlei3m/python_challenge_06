from src.controllers.natural_person_creator_controller import NaturalPersonCreatorController
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository
from src.views.natural_person_creator_view import NaturalPersonCreatorView

def natural_person_creator_composer():
    model = NaturalPersonRepository(db_connection_handler)
    controller = NaturalPersonCreatorController(model)
    view = NaturalPersonCreatorView(controller)

    return view
