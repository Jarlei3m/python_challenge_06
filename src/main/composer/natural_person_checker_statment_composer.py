from src.controllers.natural_person_checker_statment_controller import (
    NaturalPersonCheckerStatmentController
    )
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository
from src.views.natural_person_checker_statment_view import NaturalPersonCheckerStatmentView

def natural_person_checker_statment_composer():
    model = NaturalPersonRepository(db_connection_handler)
    controller = NaturalPersonCheckerStatmentController(model)
    view = NaturalPersonCheckerStatmentView(controller)

    return view
