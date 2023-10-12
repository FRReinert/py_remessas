from uuid import uuid4

from cnab.cnab import CnabName, CnabContractData, CnabBankingDataForLiquidation, CnabReceivableUnitData, CnabHeader, CnabTrail
from cnab.enums import (
    EAccountType,
    EArrangement,
    EBank,
    EContractEffect,
    EContractStatus,
    EDivisionMethod,
    EDocumentType,
    EGuaranteeType,
)
from cnab.exporters import FileExporter
from cnab.types import CnabDate, CnabDateTime, Document, Guid, Money

# properties
unique_id = 10
customer_document = Document("12345678901")

contract_data_params = {
    "key": Guid(str(uuid4())),
    "holder_document": Document("12345667801"),
    "creation_timestamp": CnabDateTime(12, 12, 2023, 0, 0, 0),
    "due_date": CnabDate(12, 12, 2023),
    "sign_date": CnabDate(12, 12, 2023),
    "effect": EContractEffect.GUARANTEE,
    "division_method": EDivisionMethod.NOMINAL_VALUE,
    "guarantee_type": EGuaranteeType.FIDUCIARY,
    "value": Money(1000),
    "guarantee_value": Money(1000),
    "percentual_ur": 100,
    "status": EContractStatus.ACTIVE_REGISTRATION,
    "qt_receivable_units": 1,
}

contract_liq_params = {
    "key": Guid(str(uuid4())),
    "bank_code": EBank.ADVANCED_CC_LTDA,
    "account_agency": "0000",
    "account_number": "1111",
    "account_digit": "9",
    "account_type": EAccountType.CHECKING_ACCOUNT,
    "document_type": EDocumentType.CPF,
    "document": Document("12345678901"),
}

contract_unit_params = {
    "contract_key": Guid(str(uuid4())),
    "receivable_unit_key": Guid(str(uuid4())),
    "transferror_document_type": EDocumentType.CPF,
    "transferror_document": Document("12345678901"),
    "accreditor_document": Document("12345678901"),
    "holder_document": Document("12345667801"),
    "arrengement_code": EArrangement.AMEX_CREDIT_CARD,
    "date_liquidation": CnabDate(12, 12, 2023),
    "receivable_unit_value": Money(1000),
    "commited_contract_value": Money(1000),
    "contract_priority": 1,
}

# contracts
contract_data = CnabContractData(**contract_data_params)
cnab_liq = CnabBankingDataForLiquidation(**contract_liq_params)
cnab_unit = CnabReceivableUnitData(**contract_unit_params)

# factories
cnab_name = CnabName(None, 'TR', 'RET', True)
cnab_head = CnabHeader(customer_document, unique_id)
cnab_trail = CnabTrail(3)

# exporter
exporter = FileExporter.export(cnab_name, cnab_head, cnab_trail, [contract_data, cnab_liq, cnab_unit], './')
