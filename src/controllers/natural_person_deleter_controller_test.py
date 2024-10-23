from src.controllers.natural_person_deleter_controller import NaturalPersonDeleterController

def test_delete_natural_person(mocker):
    mock_repository = mocker.Mock()
    controller = NaturalPersonDeleterController(mock_repository)
    controller.delete("John Doe")

    mock_repository.delete_natural_person.assert_called_once_with("John Doe")
