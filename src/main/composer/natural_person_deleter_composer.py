from src.controllers.natural_person_deleter_controller import NaturalPersonDeleterController
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository
from src.views.natural_person_deleter_view import NaturalPersonDeleterView

def natural_person_deleter_composer():
    model = NaturalPersonRepository(db_connection_handler)
    controller = NaturalPersonDeleterController(model)
    view = NaturalPersonDeleterView(controller)

    return view
