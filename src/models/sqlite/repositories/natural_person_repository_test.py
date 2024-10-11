from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.natural_person import NaturalPersonTable
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(NaturalPersonTable)],
                    [
                        NaturalPersonTable(
                            renda_mensal=5000, 
                            idade=35, 
                            nome_completo="João Silva",
                            celular="9999-8888",
                            email="joao@example.com",
                            categoria="Categoria A",
                            saldo=10000
                        ),
                        NaturalPersonTable(
                            renda_mensal=4000, 
                            idade=45, 
                            nome_completo="Maria Oliveira",
                            celular="7777-6666",
                            email="maria@example.com",
                            categoria="Categoria B",
                            saldo=15000
                        )
                    ]
                )
            ]
        )

    def __enter__(self): 
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found
    
    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self): 
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def test_list_natural_person():
    mock_connection = MockConnection()
    repo = NaturalPersonRepository(mock_connection)
    response = repo.list_natural_person()

    mock_connection.session.query.assert_called_once_with(NaturalPersonTable)
    mock_connection.session.all.assert_called_once()

    assert response[0].nome_completo == "João Silva"

def test_delete_natural_person():
    mock_connection = MockConnection()
    repo = NaturalPersonRepository(mock_connection)
    repo.delete_natural_person("NaturalPersonName")

    mock_connection.session.query.assert_called_once_with(NaturalPersonTable)
    mock_connection.session.filter.assert_called_once_with(
        NaturalPersonTable.nome_completo == "NaturalPersonName"
    )
    mock_connection.session.delete.assert_called_once()

def test_list_natural_person_no_result():
    mock_connection = MockConnectionNoResult()
    repo = NaturalPersonRepository(mock_connection)
    response = repo.list_natural_person()

    mock_connection.session.query.assert_called_once_with(NaturalPersonTable)
    mock_connection.session.all.assert_not_called()

    assert response == []
    
def test_delete_natural_person_error():
    mock_connection = MockConnectionNoResult()
    repo = NaturalPersonRepository(mock_connection)
    
    with pytest.raises(Exception):
        repo.delete_natural_person("NaturalPersonName")
    
    mock_connection.session.rollback.assert_called_once()
    