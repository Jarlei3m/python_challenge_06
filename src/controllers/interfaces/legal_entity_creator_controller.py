from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class LegalEntityData:
    faturamento: float
    idade: int
    nome_fantasia: str
    celular: str
    email_corporativo: str
    categoria: str
    saldo: float

class LegalEntityCreatorControllerInterface(ABC):
    
    @abstractmethod
    def create(self, legal_entity_info: LegalEntityData) -> None:
        pass
    