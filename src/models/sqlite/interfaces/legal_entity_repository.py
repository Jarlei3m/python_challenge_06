from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from src.models.sqlite.entities.legal_entity import LegalEntityTable

@dataclass
class LegalEntityData:
    faturamento: float
    idade: int
    nome_fantasia: str
    celular: str
    email_corporativo: str
    categoria: str
    saldo: float
    
class LegalEntityRepositoryInterface(ABC):

    @abstractmethod
    def insert_legal_entity(self, entity_data: LegalEntityData) -> None:
        pass
    
    @abstractmethod
    def list_legal_entity(self) -> List[LegalEntityTable]:
        pass
    
    @abstractmethod
    def delete_legal_entity(self, name: str) -> None:
        pass
    
    @abstractmethod
    def withdraw_cash_legal_entity(self, legal_entity_id: int, amount: float) -> None:
        pass
    
    @abstractmethod
    def check_statment_legal_entity(self, legal_entity_id: int) -> LegalEntityTable:
        pass
    