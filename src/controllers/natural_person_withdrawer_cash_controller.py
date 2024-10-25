from typing import Dict
from src.models.sqlite.interfaces.natural_person_repository import NaturalPersonRepositoryInterface

class NaturalPersonWithdrawerCashController:
    def __init__(self, legal_entity_repository: NaturalPersonRepositoryInterface):
        self.__legal_entity_repository = legal_entity_repository

    def withdraw_cash(self, withdraw_info: Dict) -> None:
        legal_entity_id = withdraw_info["id"]
        amount = withdraw_info["amount"]

        self.__validate_id(legal_entity_id)
        self.__validate_amount(amount)
        
        self.__legal_entity_repository.withdraw_cash_legal_entity(legal_entity_id, amount)
    
    def __validate_id(self, legal_entity_id: int) -> None:
        if not legal_entity_id:
            raise Exception("Any legal entity id has been informed")
    
    def __validate_amount(self, amount: float) -> None:
        if amount < 0:
            raise Exception("Invalid monthly income! It must be equal or bigger than zero.")              
          