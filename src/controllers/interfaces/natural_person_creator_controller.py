from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict

@dataclass
class NaturalPersonData:
    renda_mensal: float
    idade: int
    nome_completo: str
    celular: str
    email: str
    categoria: str
    saldo: float

class NaturalPersonCreatorControllerInterface(ABC):
    
    @abstractmethod
    def create(self, natural_person_info: NaturalPersonData) -> Dict:
        pass
