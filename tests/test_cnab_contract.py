from unittest import TestCase
from cnab.cnab import CnabContractData

from cnab.enums import EContractEffect, EContractStatus, EDivisionMethod, EGuaranteeType
from cnab.helpers import make_spaces
from cnab.types import CnabDate, CnabDateTime, Document, Guid, Money


mock_contract = {
    "key": Guid('12345678-abcd-1234-efgh-9876543210ab'),
    "holder_document": Document('1234567890'),
    "creation_timestamp": CnabDateTime(28, 10, 2020, 13, 52, 23),
    "due_date": CnabDate(28, 10, 2020),
    "sign_date": CnabDate(29, 10, 202),
    "effect": EContractEffect.GUARANTEE,
    "division_method": EDivisionMethod.NOMINAL_VALUE,
    "guarantee_type": EGuaranteeType.FIDUCIARY,
    "value": Money(1000),
    "guarantee_value": Money(500),
    "percentual_ur": 10,
    "status": EContractStatus.ACTIVE_REGISTRATION,
    "qt_receivable_units": 5,
}

expected_line = f"112345678-abcd-1234-efgh-9876543210ab000012345678902020-10-28 13:52:232020-10-280202-10-292110000000000010000000000000005001025{make_spaces(400 - 127)}"  # noqa: E501


class TestContractData(TestCase):
    def test_cnab_contract_with_valid_data(self):
        contract = CnabContractData(**mock_contract)
        self.assertEqual(contract.make_line(), expected_line)
