from typing import Dict
from src.controllers.interfaces.legal_entity_checker_statment_controller import (
    LegalEntityCheckerStatmentControllerInterface
    )
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.models.sqlite.interfaces.legal_entity_repository import LegalEntityRepositoryInterface

class LegalEntityCheckerStatmentController(LegalEntityCheckerStatmentControllerInterface):
    def __init__(self, legal_entity_repository: LegalEntityRepositoryInterface) -> None:
        self.__legal_entity_repository = legal_entity_repository

    def check_statment(self, legal_entity_id: int) -> Dict:
        check_statment_data = self.__get_statment_data_in_db(legal_entity_id)
        response = self.__format_response(check_statment_data)

        return response
        
    def __get_statment_data_in_db(self, legal_entity_id: int) -> LegalEntityTable:
        check_statment_data = (
            self.__legal_entity_repository.check_statment_legal_entity(legal_entity_id)
            )

        if not check_statment_data:
            raise HttpBadRequestError("An internal error occurred!")
        
        return check_statment_data
    
    def __format_response(self, check_statment_data: LegalEntityTable) -> Dict:
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
    