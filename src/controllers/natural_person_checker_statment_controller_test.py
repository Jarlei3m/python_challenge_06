from .natural_person_checker_statment_controller import NaturalPersonCheckerStatmentController

def test_natural_person_checker_statment(mocker):
    mock_repository = mocker.Mock()

    mock_id = 123

    controller = NaturalPersonCheckerStatmentController(mock_repository)
    controller.check_statment(mock_id)

    mock_repository.check_statment_natural_person.assert_called_once_with(mock_id)
