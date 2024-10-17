from typing import Dict
import pytest
from .natural_person_creator_controller import NaturalPersonCreatorController

class MockNaturalPersonRepository:
    def insert_natural_person(self, natural_person_info: Dict):
        pass

def test_create():
    natural_person_info = {
        "renda_mensal": 5000.0,
        "idade": 30,
        "nome_completo": "John Doe",
        "celular": "24992005011",
        "email": "johndoe@example.com",
        "categoria": "A",
        "saldo": 1000.0
    }

    controller = NaturalPersonCreatorController(MockNaturalPersonRepository())
    
    response = controller.create(natural_person_info)

    assert response["data"]["type"] == "Natural Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == natural_person_info

def test_create_error():
    natural_person_info = {
        "renda_mensal": 5000.0,
        "idade": 30,
        "nome_completo": "John#$% --- , Doe test",
        "celular": "24992005011",
        "email": "johndoe@example.com",
        "categoria": "A",
        "saldo": 1000.0
    }

    controller = NaturalPersonCreatorController(MockNaturalPersonRepository())

    with pytest.raises(Exception):
        controller.create(natural_person_info)
