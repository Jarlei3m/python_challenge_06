from src.controllers.legal_entity_deleter_controller import LegalEntityDeleterController

def test_delete_legal_entity(mocker):
    mock_repository = mocker.Mock()
    controller = LegalEntityDeleterController(mock_repository)
    controller.delete("John Doe 2")

    mock_repository.delete_legal_entity.assert_called_once_with("John Doe 2")
    