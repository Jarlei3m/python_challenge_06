from abc import ABC, abstractmethod
from typing import Dict

class NaturalPersonListerControllerInterface(ABC):
   
    @abstractmethod
    def list(self) -> Dict:
        pass
