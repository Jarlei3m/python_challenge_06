import pytest
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository
from src.models.sqlite.settings.connection import db_connection_handler
from .legal_entity_repository import LegalEntityData, LegalEntityRepository

# db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="db integration")
def test_list_natural_person():
    repo = NaturalPersonRepository(db_connection_handler)
    response = repo.list_natural_person()
    print()
    print(response)

@pytest.mark.skip(reason="db integration")
def test_delete_natural_person():
    name = "Pedro Santos"

    repo = NaturalPersonRepository(db_connection_handler)
    repo.delete_natural_person(name)

@pytest.mark.skip(reason="db integration")
def test_insert_legal_entity():
    mock_legal_entity_data = LegalEntityData(
        faturamento="faturamento",
        idade=25,
        nome_fantasia="nome fantasia",
        celular="8888-9999",
        email_corporativo="email@test.com",
        categoria="category A",
        saldo=25852.16
    )

    repo = LegalEntityRepository(db_connection_handler)
    repo.insert_legal_entity(mock_legal_entity_data)
