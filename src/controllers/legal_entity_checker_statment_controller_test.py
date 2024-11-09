from src.controllers.legal_entity_checker_statment_controller import (
    LegalEntityCheckerStatmentController
)

def test_legal_entity_checker_statment(mocker):
    mock_repository = mocker.Mock()

    mock_id = 123

    mock_repository.check_statment_legal_entity.return_value = {
        "_mapping": {
            "id": mock_id,
            "nome_fantasia": "John Doe",
            "faturamento": 5000.00,
            "idade": 30,
            "celular": "123456789",
            "email_corporativa": "john.doe@example.com",
            "categoria": "A",
            "saldo": 1000.00
        }
    }

    controller = LegalEntityCheckerStatmentController(mock_repository)
    
    controller.check_statment(mock_id)

    mock_repository.check_statment_legal_entity.assert_called_once_with(mock_id)
