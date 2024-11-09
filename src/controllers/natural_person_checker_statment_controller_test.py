from src.controllers.natural_person_checker_statment_controller import (
    NaturalPersonCheckerStatmentController
)

def test_natural_person_checker_statment(mocker):
    mock_repository = mocker.Mock()

    mock_id = 123

    mock_repository.check_statment_natural_person.return_value = {
        "_mapping": {
            "id": mock_id,
            "nome_completo": "John Doe",
            "renda_mensal": 5000.00,
            "idade": 30,
            "celular": "123456789",
            "email": "john.doe@example.com",
            "categoria": "A",
            "saldo": 1000.00
        }
    }

    controller = NaturalPersonCheckerStatmentController(mock_repository)
    
    controller.check_statment(mock_id)

    mock_repository.check_statment_natural_person.assert_called_once_with(mock_id)
    