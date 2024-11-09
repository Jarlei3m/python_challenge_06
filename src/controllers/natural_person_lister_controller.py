from typing import Dict, List
from src.controllers.interfaces.natural_person_lister_controller import (
    NaturalPersonListerControllerInterface
    )
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.entities.natural_person import NaturalPersonTable
from src.models.sqlite.interfaces.natural_person_repository import NaturalPersonRepositoryInterface


class NaturalPersonListerController(NaturalPersonListerControllerInterface):
    def __init__(self, natural_person_repository: NaturalPersonRepositoryInterface) -> None:
        self.__natural_person_repository = natural_person_repository
    
    def list(self) -> Dict:
        natural_person_list = self.__get_natural_person_list_in_db()
        response = self.__format_response(natural_person_list)

        return response

    def __get_natural_person_list_in_db(self) -> List[NaturalPersonTable]:
        natural_person_list = self.__natural_person_repository.list_natural_person()
        
        if not natural_person_list:
            raise HttpBadRequestError("An internal error occurred!")

        return natural_person_list
    
    def __format_response(self, natural_person_list: List[NaturalPersonTable]) -> Dict:
        formatted_natural_person_list = []
        for natural_person in natural_person_list:
            formatted_natural_person_list.append({
                "id": natural_person.id,
                "renda_mensal": natural_person.renda_mensal,
                "idade": natural_person.idade,
                "nome_completo": natural_person.nome_completo,
                "celular": natural_person.celular,
                "email": natural_person.email,
                "categoria": natural_person.categoria,
                "saldo": natural_person.saldo
            })
        
        return {
            "data": {
                "type": "Natural Person",
                "count": len(formatted_natural_person_list),
                "attributes": formatted_natural_person_list
            }
        }
    