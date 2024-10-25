from typing import Dict, List
from src.controllers.interfaces.legal_entity_lister_controller import (
    LegalEntityListerControllerInterface
    )
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository

class LegalEntityListerController(LegalEntityListerControllerInterface):
    def __init__(self, legal_entity_repository: LegalEntityRepository):
        self.__legal_entity_repository = legal_entity_repository
    
    def list(self) -> Dict:
        legal_entity_list = self.__get_legal_entity_list_in_db()
        response = self.__format_response(legal_entity_list)

        return response
    
    def __get_legal_entity_list_in_db(self) -> None:
        legal_entity_list = self.__legal_entity_repository.list_legal_entity()
        
        if not legal_entity_list:
            raise Exception("An internal error occurred!")

        return legal_entity_list

    def __format_response(self, legal_entity_list: List[LegalEntityTable]):
        formatted_legal_entity_list = []
        for legal_entity in legal_entity_list:
            formatted_legal_entity_list.append({
                "faturamento": legal_entity.faturamento,
                "idade": legal_entity.idade,
                "nome_fantasia": legal_entity.nome_fantasia,
                "celular": legal_entity.celular,
                "email_corporativo": legal_entity.email_corporativo,
                "categoria": legal_entity.categoria,
                "saldo": legal_entity.saldo
            })
        
        return {
            "data": {
                "type": "Legal Entity",
                "count": len(formatted_legal_entity_list),
                "attributes": formatted_legal_entity_list
            }
        }
