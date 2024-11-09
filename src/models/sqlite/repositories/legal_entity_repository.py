from dataclasses import dataclass
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.models.sqlite.interfaces.legal_entity_repository import LegalEntityRepositoryInterface

@dataclass
class LegalEntityData:
    faturamento: float
    idade: int
    nome_fantasia: str
    celular: str
    email_corporativo: str
    categoria: str
    saldo: float

class LegalEntityRepository(LegalEntityRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
    
    def insert_legal_entity(self, entity_data: LegalEntityData) -> None:
        with self.__db_connection as database:
            try:
                legal_entity_data = LegalEntityTable(
                    faturamento=entity_data["faturamento"],
                    idade=entity_data["idade"],
                    nome_fantasia=entity_data["nome_fantasia"],
                    celular=entity_data["celular"],
                    email_corporativo=entity_data["email_corporativo"],
                    categoria=entity_data["categoria"],
                    saldo=entity_data["saldo"]
                )
                database.session.add(legal_entity_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_legal_entity(self) -> List[LegalEntityTable]:
        with self.__db_connection as database:
            try:
                legal_entity = database.session.query(LegalEntityTable).all()
                return legal_entity
            except NoResultFound:
                return []
    
    def delete_legal_entity(self, name: str) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session
                        .query(LegalEntityTable)
                        .filter(LegalEntityTable.nome_fantasia == name)
                        .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def withdraw_cash_legal_entity(self, legal_entity_id: int, amount: float) -> None:
        with self.__db_connection as database:
            try:
                legal_entity = (
                    database.session
                    .query(LegalEntityTable)
                    .filter(LegalEntityTable.id == legal_entity_id)
                    .one()
                )

                withdraw_limit_allowed = 10000
                if amount > withdraw_limit_allowed:
                    error_message = "The amount exceeded the withdrawal limit for this account."
                    raise ValueError(error_message)

                if legal_entity.saldo >= amount:
                    legal_entity.saldo -= amount
                else:
                    error_message = "Insufficient balance for this withdrawal."
                    raise ValueError(error_message)
                
                database.session.commit()
            except NoResultFound as exc:
                raise ValueError("Legal entity not found") from exc

            except Exception as exception:
                database.session.rollback()
                raise exception

    def check_statment_legal_entity(self, legal_entity_id: int) -> LegalEntityTable:
        with self.__db_connection as database:
            try:
                legal_entity = (
                    database.session
                    .query(LegalEntityTable)
                    .filter(LegalEntityTable.id == legal_entity_id)
                    .with_entities(
                        LegalEntityTable.nome_fantasia,
                        LegalEntityTable.saldo,
                        LegalEntityTable.faturamento
                    )
                    .one()
                )

                return legal_entity
            except NoResultFound:
                return None
                