from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.natural_person import NaturalPersonTable

class NaturalPersonRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

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
            