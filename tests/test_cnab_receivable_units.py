import pytest
from cnab.enums import (
    EArrangement,
    EDocumentType,
    ETransaction,
)
from cnab.helpers import make_spaces
from cnab.types import CnabDate, Document, Guid, Money
from cnab.regress import CnabReturnTypeThree


@pytest.mark.parametrize(
    "contract_key, receivable_unit_key, transferror_document_type, transferror_document, accreditor_document, holder_document, arrengement_code, date_liquidation, receivable_unit_value, commited_contract_value, contract_priority, unique_id, expected_line",  # noqa: E501
    [
        (
            Guid("12345678-1234-1234-1234-123456789abc"),
            Guid("87654321-1234-1234-1234-123456789abc"),
            EDocumentType.CPF,
            Document("33333333333"),
            Document("11111111110"),
            Document("55555555555"),
            EArrangement.AMEX_CREDIT_CARD,
            CnabDate(1, 1, 2000),
            Money(400),
            Money(400),
            1,
            ETransaction.RECEIVABLES_UNIT_DATA,
            "312345678-1234-1234-1234-123456789abc cpf000333333333330001111111111000055555555555ACC2000-01-010000000000004000000000000004001"
            + make_spaces(400 - 127)
        )
    ],
    ids=["test happy path"],
)
def test_make_line(
    contract_key,
    receivable_unit_key,
    transferror_document_type,
    transferror_document,
    accreditor_document,
    holder_document,
    arrengement_code,
    date_liquidation,
    receivable_unit_value,
    commited_contract_value,
    contract_priority,
    unique_id,
    expected_line,
):
    cnab_instance = CnabReturnTypeThree(
        contract_key,
        receivable_unit_key,
        transferror_document_type,
        transferror_document,
        accreditor_document,
        holder_document,
        arrengement_code,
        date_liquidation,
        receivable_unit_value,
        commited_contract_value,
        contract_priority,
        unique_id,
    )
    assert cnab_instance.make_line() == expected_line
