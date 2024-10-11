import pytest
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository
from src.models.sqlite.settings.connection import db_connection_handle

db_connection_handle.connect_to_db()

@pytest.mark.skip(reason="db integration")
def test_list_natural_person():
    repo = NaturalPersonRepository(db_connection_handle)
    response = repo.list_natural_person()
    print()
    print(response)

@pytest.mark.skip(reason="db integration")
def test_delete_natural_person():
    name = "Pedro Santos"

    repo = NaturalPersonRepository(db_connection_handle)
    repo.delete_natural_person(name)
