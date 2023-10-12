from cnab.cnab import CnabHeader, CnabReceivableUnitData, CnabTrail
from cnab.enums import EArrangement
from cnab.exporters import FileExporter
from cnab.types import CnabDate, Document, Guid, Money

unique_id = Guid("12345678-1234-1234-1234-123456789abc")
contract_key = Guid("12345678-1234-1234-1234-123456789abc")
receivable_unit_key = Guid("12345678-1234-1234-1234-123456789abc")
customer_document = Document("11111111111")
transferror_document = Document("11111111111")
accreditor_document = Document("11111111111")
holder_document = Document("11111111111")
arrengement_code = EArrangement.AMEX_CREDIT_CARD
date_liquidation = CnabDate(1, 12, 2022)  # 1/12/2022
receivable_unit_value = Money(1000)  # R$ 10,00
commited_contract_value = Money(1000)  # R$ 10,00
contract_priority = 1

header = CnabHeader(customer_document, unique_id)
trail = CnabTrail(1)
contract_one = CnabReceivableUnitData(
    contract_key=contract_key,
    receivable_unit_key=receivable_unit_key,
    transferror_document=transferror_document,
    accreditor_document=accreditor_document,
    holder_document=holder_document,
    arrengement_code=arrengement_code,
    date_liquidation=date_liquidation,
    receivable_unit_value=receivable_unit_value,
    commited_contract_value=commited_contract_value,
    contract_priority=contract_priority,
)

FileExporter.export(header, trail, [contract_one], f"./{unique_id}.cnab")
