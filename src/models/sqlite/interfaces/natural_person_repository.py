from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from src.models.sqlite.entities.natural_person import NaturalPersonTable

@dataclass
class NaturalPersonData:
    renda_mensal: float
    idade: int
    nome_completo: str
    celular: str
    email: str
    categoria: str
    saldo: float

class NaturalPersonRepositoryInterface(ABC):

    @abstractmethod
    def insert_natural_person(self, person_data: NaturalPersonData) -> None:
        pass
    
    @abstractmethod
    def list_natural_person(self) -> List[NaturalPersonTable]:
        pass
    
    @abstractmethod
    def delete_natural_person(self, name: str) -> None:
        pass
    
    @abstractmethod
    def withdraw_cash_natural_person(self, natural_person_id: int, amount: float) -> None:
        pass
    
    @abstractmethod
    def check_statment_natural_person(self, natural_person_id: int) -> NaturalPersonTable:
        pass
  