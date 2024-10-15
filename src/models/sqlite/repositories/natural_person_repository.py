from dataclasses import dataclass
from typing import List
from sqlalchemy.orm.exc import NoResultFound
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

class NaturalPersonRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_natural_person(self, person_data: NaturalPersonData) -> None:
        with self.__db_connection as database:
            try:
                natural_person_data = NaturalPersonTable(
                    renda_mensal=person_data.renda_mensal,
                    idade=person_data.idade,
                    nome_completo=person_data.nome_completo,
                    celular=person_data.celular,
                    email=person_data.email,
                    categoria=person_data.categoria,
                    saldo=person_data.saldo
                )
                database.session.add(natural_person_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_natural_person(self) -> List[NaturalPersonTable]:
        with self.__db_connection as database:
            try:
                natural_person = database.session.query(NaturalPersonTable).all()
                return natural_person
            except NoResultFound:
                return []
    
    def delete_natural_person(self, name: str) -> None:
        with self.__db_connection as database:
            try:
                (
                  database.session
                      .query(NaturalPersonTable)
                      .filter(NaturalPersonTable.nome_completo == name)
                      .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def withdraw_cash_natural_person(self, natural_person_id: int, amount: float) -> None:
        with self.__db_connection as database:
            try:
                natural_person = (
                    database.session
                    .query(NaturalPersonTable)
                    .filter(NaturalPersonTable.id == natural_person_id)
                    .one()
                )

                if natural_person.saldo >= amount:
                    natural_person.saldo -= amount
                else:
                    error_message = "Insufficient balance for this withdrawal."
                    raise ValueError(error_message)
                
                database.session.commit()
            except NoResultFound as exc:
                raise ValueError("Natural person not found") from exc

            except Exception as exception:
                database.session.rollback()
                raise exception

    def check_statment_natural_person(self, natural_person_id: int) -> NaturalPersonTable:
        with self.__db_connection as database:
            try:
                natural_person = (
                    database.session
                    .query(NaturalPersonTable)
                    .filter(NaturalPersonTable.id == natural_person_id)
                    .with_entities(
                        NaturalPersonTable.nome_completo,
                        NaturalPersonTable.saldo,
                        NaturalPersonTable.renda_mensal
                    )
                    .one()
                )

                return natural_person
            except NoResultFound:
                return None
            