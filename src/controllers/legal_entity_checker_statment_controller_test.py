from src.controllers.legal_entity_checker_statment_controller import (
    LegalEntityCheckerStatmentController
    )

def test_legal_entity_checker_statment(mocker):
    mock_repository = mocker.Mock()

    mock_id = 123

    controller = LegalEntityCheckerStatmentController(mock_repository)
    controller.check_statment(mock_id)

    mock_repository.check_statment_legal_entity.assert_called_once_with(mock_id)
    