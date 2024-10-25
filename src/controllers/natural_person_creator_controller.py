from dataclasses import dataclass
import re
from typing import Dict
from src.controllers.interfaces.natural_person_creator_controller import (
    NaturalPersonCreatorControllerInterface
    )
from src.models.sqlite.interfaces.natural_person_repository import NaturalPersonRepositoryInterface

@dataclass
class NaturalPersonData:
    renda_mensal: float
    idade: int
    nome_completo: str
    celular: str
    email: str
    categoria: str
    saldo: float

class NaturalPersonCreatorController(NaturalPersonCreatorControllerInterface):
    def __init__(self, natural_person_repository: NaturalPersonRepositoryInterface) -> None:
        self.__natural_person_repository = natural_person_repository
    
    def create(self, natural_person_info: NaturalPersonData) -> Dict:
        renda_mensal = natural_person_info["renda_mensal"]
        nome_completo = natural_person_info["nome_completo"]
        celular = natural_person_info["celular"]
        email = natural_person_info["email"]

        self.__validate_name(nome_completo)
        self.__validate_email(email)
        self.__validate_cell_phone(celular)
        self.__validate_monthly_income(renda_mensal)
        self.__insert_natural_person_in_db(natural_person_info)

        formatted_reponse = self.__format_response(natural_person_info)
        return formatted_reponse

    def __validate_name(self, nome_completo: str) ->  None:
        nome_completo = nome_completo.strip()

        non_valid_characters = re.compile(r'[^a-zA-Z ]')

        if non_valid_characters.search(nome_completo):
            raise Exception("Invalid name!")

        if "  " in nome_completo:
            raise Exception("Invalid name! Consecutive spaces are not allowed.")
    
    def __validate_email(self, email: str) -> None:
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

        if not email_pattern.match(email):
            raise Exception("Invalid email address!")
    
    def __validate_cell_phone(self, celular: str) -> None:
        celular_pattern = re.compile(r'^(\+55\s?)?(\(?\d{2}\)?)\s?\d{5}-?\d{4}$')

        if not celular_pattern.match(celular):
            raise Exception("Invalid cell phone number!")
        
    def __validate_monthly_income(self, renda_mesal: float) -> None:
        if renda_mesal < 0:
            raise Exception("Invalid monthly income! It must be equal or bigger than zero.")
    
    def __insert_natural_person_in_db(self, natural_person_info: NaturalPersonData) -> None:
        self.__natural_person_repository.insert_natural_person(natural_person_info)
    
    def __format_response(self, natural_person_info: NaturalPersonData) -> Dict:
        return {
            "data": {
                "type": "Natural Person",
                "count": 1,
                "attributes": natural_person_info
            }
        }
    