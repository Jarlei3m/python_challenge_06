from typing import Dict
from src.controllers.interfaces.natural_person_checker_statment_controller import (
    NaturalPersonCheckerStatmentControllerInterface
    )
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.entities.natural_person import NaturalPersonTable
from src.models.sqlite.interfaces.natural_person_repository import NaturalPersonRepositoryInterface

class NaturalPersonCheckerStatmentController(NaturalPersonCheckerStatmentControllerInterface):
    def __init__(self, natural_person_repository: NaturalPersonRepositoryInterface) -> None:
        self.__natural_person_repository = natural_person_repository

    def check_statment(self, natural_person_id: int) -> Dict:
        check_statment_data = self.__get_statment_data_in_db(natural_person_id)
        response = self.__format_response(check_statment_data)

        return response
        
    def __get_statment_data_in_db(self, natural_person_id: int) -> NaturalPersonTable:
        check_statment_data = (
            self.__natural_person_repository.check_statment_natural_person(natural_person_id)
            )

        if not check_statment_data:
            raise HttpBadRequestError("An internal error occurred!")
        
        return check_statment_data
    
    def __format_response(self, check_statment_data: NaturalPersonTable) -> Dict:
        if hasattr(check_statment_data, '_mapping'):
            attributes = dict(check_statment_data._mapping)
        else:
            attributes = check_statment_data
    
        return {
            "data": {
                "type": "Natural Person",
                "count": 1,
                "attributes": attributes
            }
        }
    