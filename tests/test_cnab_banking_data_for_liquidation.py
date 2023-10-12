import pytest
from cnab.enums import (
    EAccountType,
    EBank,
    EDocumentType,
    ETransaction,
)
from cnab.cnab import CnabBankingDataForLiquidation


@pytest.mark.parametrize(
    "key, bank_code, account_agency, account_number, account_digit, account_type, document_type, document, unique_id, expected_line",
    [
        (
            "12345678-1234-5678-1234-567812345678",
            EBank.BANCO_BRADESCARD_SA,
            "1234",
            "5678",
            "9",
            EAccountType.CHECKING_ACCOUNT,
            EDocumentType.CPF,
            "12345678901",
            ETransaction.BANK_LIQUIDATION_DATA,
            "212345678-1234-5678-1234-567812345678063123456789CC cpf12345678901"
            + " " * 325,
        ),
        (
            "00000000-0000-0000-0000-000000000000",
            "479",
            "0000",
            "0000",
            "0",
            EAccountType.SAVINGS_ACCOUNT,
            EDocumentType.CNPJ,
            "00000000000000",
            ETransaction.BANK_LIQUIDATION_DATA,
            "200000000-0000-0000-0000-000000000000479000000000PPcnpj00000000000000"
            + " " * 325,
        ),
        (
            "00000000-0000-0000-0000-000000000000",
            479,
            "0000",
            "0000",
            "0",
            EAccountType.SAVINGS_ACCOUNT,
            EDocumentType.CNPJ,
            "00000000000000",
            ETransaction.BANK_LIQUIDATION_DATA,
            "200000000-0000-0000-0000-000000000000479000000000PPcnpj00000000000000"
            + " " * 325,
        ),
    ],
    ids=[
        "Happy path",
        "Using bank code as string",
        "Using bank code as a integer",
    ],
)
def test_make_line(
    key,
    bank_code,
    account_agency,
    account_number,
    account_digit,
    account_type,
    document_type,
    document,
    unique_id,
    expected_line,
):
    cnab_data = CnabBankingDataForLiquidation(
        key=key,
        bank_code=bank_code,
        account_agency=account_agency,
        account_number=account_number,
        account_digit=account_digit,
        account_type=account_type,
        document_type=document_type,
        document=document,
        unique_id=unique_id,
    )
    line = cnab_data.make_line()
    assert line == expected_line


def test_make_line_with_large_bank_code_str_should_raise_valuerror():
    data = {
        "key": "12345678-1234-5678-1234-567812345678",
        "bank_code": "INVALID_BANK_CODE",
        "account_agency": "1234",
        "account_number": "5678",
        "account_digit": "9",
        "account_type": EAccountType.CHECKING_ACCOUNT,
        "document_type": EDocumentType.CPF,
        "document": "12345678901",
        "unique_id": ETransaction.BANK_LIQUIDATION_DATA,
    }
    with pytest.raises(ValueError):
        CnabBankingDataForLiquidation(**data).make_line()


def test_make_line_with_large_bank_code_int_should_raise_valuerror():
    data = {
        "key": "12345678-1234-5678-1234-567812345678",
        "bank_code": 1000,
        "account_agency": "1234",
        "account_number": "5678",
        "account_digit": "9",
        "account_type": EAccountType.CHECKING_ACCOUNT,
        "document_type": EDocumentType.CPF,
        "document": "12345678901",
        "unique_id": ETransaction.BANK_LIQUIDATION_DATA,
    }
    with pytest.raises(ValueError):
        CnabBankingDataForLiquidation(**data).make_line()
