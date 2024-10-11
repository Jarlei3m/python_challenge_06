from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

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

def test_list_natural_person():
    mock_connection = MockConnection()
    repo = NaturalPersonRepository(mock_connection)
    response = repo.list_natural_person()

    mock_connection.session.query.assert_called_once_with(NaturalPersonTable)
    mock_connection.session.all.assert_called_once()

    assert response[0].nome_completo == "João Silva"
