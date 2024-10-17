from dataclasses import dataclass
import re
from typing import Dict
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository

@dataclass
class LegalEntityData:
    faturamento: float
    idade: int
    nome_fantasia: str
    celular: str
    email_corporativo: str
    categoria: str
    saldo: float

class LegalEntityCreatorController:
    def __init__(self, legal_entity_repository: LegalEntityRepository):
        self.__legal_entity_repository = legal_entity_repository

    def create(self, legal_entity_info: LegalEntityData) -> None:
        faturamento = legal_entity_info["faturamento"]
        nome_fantasia = legal_entity_info["nome_fantasia"]
        celular = legal_entity_info["celular"]
        email_corporativo = legal_entity_info["email_corporativo"]

        self.__validate_name(nome_fantasia)
        self.__validate_email(email_corporativo)
        self.__validate_cell_phone(celular)
        self.__validate_revenue(faturamento)
        self.__insert_legal_entity_in_db(legal_entity_info)

        response = self.__format_response(legal_entity_info)
        return response

    def __validate_name(self, nome_fantasia: str) -> None:
        nome_fantasia = nome_fantasia.strip()

        no_valid_characters = re.compile(r'[^a-zA-Z]')

        if no_valid_characters.search(nome_fantasia):
            raise Exception("Invalid trade name")
        
        if "  " in nome_fantasia:
            raise Exception("Invalid name! Consecutive spaces are not allowed.")
    
    def __validate_email(self, email: str) -> None:
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

        if not email_pattern.match(email):
            raise Exception("Invalid email address!")
          
    def __validate_cell_phone(self, celular: str) -> None:
        celular_pattern = re.compile(r'^(\+55\s?)?(\(?\d{2}\)?)\s?\d{5}-?\d{4}$')

        if not celular_pattern.match(celular):
            raise Exception("Invalid cell phone number!")
    
    def __validate_revenue(self, faturamento: float) -> None:
        if faturamento < 0:
            raise Exception("Invalid monthly income! It must be equal or bigger than zero.")
    
    def __insert_legal_entity_in_db(self, legal_entity_info: LegalEntityData) -> None:
        self.__legal_entity_repository.insert_legal_entity(legal_entity_info)
    
    def __format_response(self, legal_entity_info: LegalEntityData) -> Dict:
        return {
            "data": {
                "type": "Legal Entity",
                "count": 1,
                "attributes": legal_entity_info
            }
        }
    