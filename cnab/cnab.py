from dataclasses import dataclass
from datetime import datetime

from cnab.enums import (
    EAccountType,
    EArrangement,
    EBank,
    EContractEffect,
    EContractStatus,
    EDivisionMethod,
    EDocumentType,
    EGuaranteeType,
    ETransaction,
)
from cnab.interfaces import ICnabLine, ICnabName
from cnab.types import CnabDate, CnabDateTime, Document, Guid, Money


@dataclass
class CnabName(ICnabName):
    last_used_filename: str
    service_prefix: str
    extension: str
    first_file: bool = False

    def _get_last_used_filename(self):
        data = self.last_used_filename.split('.')[0]
        if len(data) != 8:
            raise ValueError('Invalid cnab filename')
        return data

    def _format_service_prefix(self) -> str:
        if len(self.service_prefix) != 2:
            raise ValueError("service prefix should contain 2 characters")

        if ord(self.service_prefix[0]) > 90 or ord(self.service_prefix[0]) < 65:
            raise ValueError("only characters are allowed in service prefix")

        if ord(self.service_prefix[1]) > 90 or ord(self.service_prefix[1]) < 65:
            raise ValueError("only characters are allowed in service prefix")

        return self.service_prefix.upper()

    def _get_last_code_from_filename(self):
        return self._get_last_used_filename()[6:8]

    def _is_last_file_from_other_day(self):
        now = datetime.now()
        day = str(now.day).zfill(2)
        month = str(now.month).zfill(2)
        return f"{day}{month}" != self._get_last_used_filename()[2:6]

    def _format_code(self):
        """
        HEX system will give us 256 files per day per customer
        hopefully this is enough
        """

        if self._is_last_file_from_other_day():
            return '00'

        last_code = self._get_last_code_from_filename()
        new_number = int(last_code, 16) + 0x1
        return hex(new_number).split('0x')[1].upper()

    def _format_extension(self):
        if len(self.extension) != 3:
            raise ValueError("extension should have 3 characters")
        return self.extension.upper()

    def _format_date(self):
        now = datetime.now()
        day = str(now.day).zfill(2)
        month = str(now.month).zfill(2)
        return f"{day}{month}"

    def make_name(self):
        if self.first_file:
            return f"{self._format_service_prefix()}{self._format_date()}00.{self._format_extension()}"
        return f"{self._format_service_prefix()}{self._format_date()}{self._format_code()}.{self._format_extension()}"


@dataclass
class CnabHeader(ICnabLine):
    customer_document: Document
    unique_id: int

    def _generate_blank_spaces(self) -> str:
        return " " * 354

    def _generate_unique_id(self) -> str:
        return f'{self.unique_id:07d}'

    def make_line(self):
        return f'02RETORNO{self._generate_unique_id()}1CONTRATO{self.customer_document}{self._generate_blank_spaces()}'


@dataclass
class CnabTrail(ICnabLine):
    contract_amount: int

    def _generate_blank_spaces(self) -> str:
        return " " * 392

    def _generate_contract_qt(self):
        return f"{self.contract_amount:07d}"

    def make_line(self):
        return f'9{self._generate_contract_qt()}{self._generate_blank_spaces()}'


@dataclass
class CnabContractData(ICnabLine):
    """Cnab regress contract data"""

    key: Guid
    holder_document: Document
    creation_timestamp: CnabDateTime
    due_date: CnabDate
    sign_date: CnabDate
    effect: EContractEffect
    division_method: EDivisionMethod
    guarantee_type: EGuaranteeType
    value: Money
    guarantee_value: Money
    percentual_ur: int
    status: EContractStatus
    qt_receivable_units: int
    unique_id: ETransaction = ETransaction.CONTRACT_DATA

    def _generate_blank_spaces(self) -> str:
        return " " * 378

    def make_line(self):
        return f"{self.unique_id}{self.key}{self.holder_document}{self.creation_timestamp}{self.due_date}{self.sign_date}{self.effect}{self.division_method}{self.guarantee_type}{self.value}{self.guarantee_value}{self.percentual_ur}{self.status}{self.qt_receivable_units}{self._generate_blank_spaces()}"  # noqa: E501


@dataclass
class CnabBankingDataForLiquidation(ICnabLine):
    """Cnab regress data for liquidation"""

    key: Guid
    bank_code: EBank | int | str
    account_agency: str
    account_number: str
    account_digit: str
    account_type: EAccountType
    document_type: EDocumentType
    document: Document
    unique_id: ETransaction = ETransaction.BANK_LIQUIDATION_DATA

    def _generate_bank_code(self) -> str:
        if isinstance(self.bank_code, EBank):
            f_bank = str(self.bank_code)

        elif isinstance(self.bank_code, str):
            if len(self.bank_code) > 3:
                raise ValueError("Bank code should not be biger then 3 digits")

            f_bank = self.bank_code.zfill(3)

        elif isinstance(self.bank_code, int):
            if self.bank_code > 999:
                raise ValueError("Bank code should not be bigger then 999")

            f_bank = str(self.bank_code).zfill(3)

        return f"{f_bank}"

    def _generate_blank_spaces(self) -> str:
        return " " * 325

    def make_line(self):
        return f"{self.unique_id}{self.key}{self._generate_bank_code()}{self.account_agency}{self.account_number}{self.account_digit}{self.account_type}{self.document_type}{self.document}{self._generate_blank_spaces()}"  # noqa: E501


@dataclass
class CnabReceivableUnitData(ICnabLine):
    """Cnab regress receivable unit data"""

    contract_key: Guid
    receivable_unit_key: Guid
    transferror_document_type: EDocumentType
    transferror_document: Document
    accreditor_document: Document
    holder_document: Document
    arrengement_code: EArrangement
    date_liquidation: CnabDate
    receivable_unit_value: Money
    commited_contract_value: Money
    contract_priority: int
    unique_id: ETransaction = ETransaction.RECEIVABLES_UNIT_DATA

    def _generate_blank_spaces(self) -> str:
        return " " * 233

    def make_line(self):
        return f"{self.unique_id}{self.contract_key}{self.transferror_document_type}{self.transferror_document}{self.accreditor_document}{self.holder_document}{self.arrengement_code}{self.date_liquidation}{self.receivable_unit_value}{self.commited_contract_value}{self.contract_priority}{self._generate_blank_spaces()}"  # noqa: E501
