from typing import Dict

import pytest

from .legal_entity_creator_controller import LegalEntityCreatorController

class MockLegalEntityRepository:
    def insert_legal_entity(self, entity_data: Dict) -> None:
        pass
        
def test_create():
    legal_entity_info = {
        "faturamento": 500000.0,
        "idade": 30,
        "nome_fantasia": "DBA",
        "celular": "24992005011",
        "email_corporativo": "dba@example.com",
        "categoria": "B",
        "saldo": 8524123.57
    }

    controller = LegalEntityCreatorController(MockLegalEntityRepository())
    response = controller.create(legal_entity_info)

    assert response["data"]["type"] == "Legal Entity"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == legal_entity_info

def test_create_error():
    legal_entity_info = {
        "faturamento": 500000.0,
        "idade": 30,
        "nome_fantasia": "DBA",
        "celular": "24992005011123",
        "email_corporativo": "dba@example.com",
        "categoria": "B",
        "saldo": 8524123.57
    }

    controller = LegalEntityCreatorController(MockLegalEntityRepository())

    with pytest.raises(Exception):
        controller.create(legal_entity_info)
        