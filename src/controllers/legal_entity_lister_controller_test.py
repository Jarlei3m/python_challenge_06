
from src.controllers.legal_entity_lister_controller import LegalEntityListerController
from src.models.sqlite.entities.legal_entity import LegalEntityTable


class MockLegalEntityRepository:
    def list_legal_entity(self):
        return [
            LegalEntityTable(
                id=1234,
                faturamento=500000.0,
                idade=30,
                nome_fantasia="DBA",
                celular="24992005011",
                email_corporativo="dba@example.com",
                categoria="B",
                saldo=8524123.57
            ),
            LegalEntityTable(
                id=5678,
                faturamento=380000.0,
                idade=35,
                nome_fantasia="DBAtest",
                celular="24992004321",
                email_corporativo="dbatest@example.com",
                categoria="B",
                saldo=5524024.74
            )
        ]

def test_list_legal_entity():
    controller = LegalEntityListerController(MockLegalEntityRepository())

    response = controller.list()

    expected_response = {
        'data': 
            {
                'type': 'Legal Entity', 
                'count': 2, 
                'attributes': [
                    {
                        'faturamento': 500000.0,
                         'idade': 30,
                         'nome_fantasia': 'DBA',
                         'celular': '24992005011',
                         'email_corporativo': 'dba@example.com',
                         'categoria': 'B',
                         'saldo': 8524123.57
                    },
                    {
                        'faturamento': 380000.0,
                         'idade': 35,
                         'nome_fantasia': 'DBAtest',
                         'celular': '24992004321',
                         'email_corporativo': 'dbatest@example.com',
                         'categoria': 'B',
                         'saldo': 5524024.74
                    }
                ]
            }
        }

    assert expected_response == response
    