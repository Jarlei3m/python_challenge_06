from abc import ABC, abstractmethod
from typing import Dict

class NaturalPersonWithdrawerCashControllerInterface(ABC):
    
    @abstractmethod
    def withdraw_cash(self, withdraw_info: Dict) -> None:
        pass
    