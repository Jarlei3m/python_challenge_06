from abc import ABC, abstractmethod
from typing import Dict

class NaturalPersonCheckerStatmentControllerInterface(ABC):
    
    @abstractmethod
    def check_statment(self, natural_person_id: int) -> Dict:
        pass
    