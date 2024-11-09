from typing import Dict
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.interfaces.natural_person_repository import NaturalPersonRepositoryInterface
from src.controllers.interfaces.natural_person_withdrawer_cash_controller import (
    NaturalPersonWithdrawerCashControllerInterface
    )

class NaturalPersonWithdrawerCashController(NaturalPersonWithdrawerCashControllerInterface):
    def __init__(self, natural_person_repository: NaturalPersonRepositoryInterface):
        self.__natural_person_repository = natural_person_repository

    def withdraw_cash(self, withdraw_info: Dict) -> None:
        natural_person_id = withdraw_info["id"]
        amount = withdraw_info["amount"]

        self.__validate_id(natural_person_id)
        self.__validate_amount(amount)
        
        self.__natural_person_repository.withdraw_cash_natural_person(natural_person_id, amount)
    
    def __validate_id(self, natural_person_id: int) -> None:
        if not natural_person_id:
            raise HttpBadRequestError("Any legal entity id has been informed")
    
    def __validate_amount(self, amount: float) -> None:
        if amount < 0:
            raise HttpBadRequestError(
                "Invalid monthly income! It must be equal or bigger than zero."
                )              
          