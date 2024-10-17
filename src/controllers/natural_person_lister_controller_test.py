from src.controllers.natural_person_lister_controller import NaturalPersonListerController
from src.models.sqlite.entities.natural_person import NaturalPersonTable

class MockNaturalPersonRepository:
    def list_natural_person(self):
        return [
            NaturalPersonTable(
                id=1234,
                renda_mensal=5000.0,
                idade=30,
                nome_completo="John Doe",
                celular="24992005011",
                email="johndoe@example.com",
                categoria="A",
                saldo=1000.0
            ),
            NaturalPersonTable(
                id=5678,
                renda_mensal=1000.0,
                idade=20,
                nome_completo="John Doe 2",
                celular="24992001234",
                email="2johndoe2@example.com",
                categoria="A",
                saldo=100.0
            )
        ]

def test_list_natural_person():
    controller = NaturalPersonListerController(MockNaturalPersonRepository())

    response = controller.list()
    
    expected_response = {
        'data': 
            {
              'type': 'Natural Person', 
              'count': 2, 
              'attributes': [
                  {
                      'id': 1234,
                      'renda_mensal': 5000.0,
                      'idade': 30,
                      'nome_completo': 'John Doe',
                      'celular': '24992005011',
                      'email': 'johndoe@example.com',
                      'categoria': 'A',
                      'saldo': 1000.0
                    },
                    {
                      'id': 5678,
                      'renda_mensal': 1000.0,
                      'idade': 20,
                      'nome_completo': 'John Doe 2',
                      'celular': '24992001234',
                      'email': '2johndoe2@example.com',
                      'categoria': 'A',
                      'saldo': 100.0
                    }
                ]
            }
    }

    assert response == expected_response
