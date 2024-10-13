from dataclasses import dataclass
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

class LegalEntityRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
    
    def insert_legal_entity(self, entity_data: LegalEntityData) -> None:
        with self.__db_connection as database:
            try:
                legal_entity_data = LegalEntityTable(
                    faturamento=entity_data.faturamento,
                    idade=entity_data.idade,
                    nome_fantasia=entity_data.nome_fantasia,
                    celular=entity_data.celular,
                    email_corporativo=entity_data.email_corporativo,
                    categoria=entity_data.categoria,
                    saldo=entity_data.saldo
                )
                database.session.add(legal_entity_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
