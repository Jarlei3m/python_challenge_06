
from .natural_person_withdrawer_cash_controller import NaturalPersonWithdrawerCashController

def test_legal_entity_withdrawer_cash(mocker):
    mocke_repository = mocker.Mock()

    withdraw_info = {
        "id": 1234,
        "amount": 13.56
    }

    controller = NaturalPersonWithdrawerCashController(mocke_repository)
    controller.withdraw_cash(withdraw_info)

    mocke_repository.withdraw_cash_legal_entity.assert_called_once_with(
        withdraw_info['id'], 
        withdraw_info['amount']
      )
    