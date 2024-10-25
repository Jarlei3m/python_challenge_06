from abc import ABC, abstractmethod
from typing import Dict

class LegalEntityListerControllerInterface(ABC):
   
    @abstractmethod
    def list(self) -> Dict:
        pass
