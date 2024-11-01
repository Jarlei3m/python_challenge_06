from abc import ABC, abstractmethod
from typing import Dict

class LegalEntityCheckerStatmentControllerInterface(ABC):
    
    @abstractmethod
    def check_statment(self, legal_entity_id: int) -> Dict:
        pass
    