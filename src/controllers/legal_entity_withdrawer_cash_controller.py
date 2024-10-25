from typing import Dict
from src.controllers.interfaces.legal_entity_withdrawer_cash_controller import (
    LegalEntityWithdrawerCashControllerInterface
    )
from src.models.sqlite.interfaces.legal_entity_repository import LegalEntityRepositoryInterface

class LegalEntityWithdrawerCashController(LegalEntityWithdrawerCashControllerInterface):
    def __init__(self, legal_entity_repository: LegalEntityRepositoryInterface):
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
          