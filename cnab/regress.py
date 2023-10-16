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
from cnab.helpers import left_justify, make_spaces
from cnab.interfaces import ICnabLine, ICnabName, ICnabTrail
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
class CnabReturnHeader(ICnabLine):
    num_sequencial: int  # 6
    documento_cliente: Document

    def _make_date(self) -> str:
        now = datetime.now()
        return f"{now.day.zfill(2)}{now.month.zfill(2)}{now.year[2:]}"

    def make_line(self):
        content = f'02RETORNO{self.num_sequencial:07d}1{left_justify("CONTRATO",15)}{self.documento_cliente}'  # noqa: E501
        return f"{content}{make_spaces(400 - len(content))}"


@dataclass
class CnabReturnTrail(ICnabTrail):
    """
    Cnab Trail Implementation
    """

    qt_contratos: int = 0  # 7

    def make_line(self):
        content = f'9{self.contract_amount:07d}'
        return f"{content}{make_spaces(400 - len(content))}"


@dataclass
class CnabReturnTypeOne(ICnabLine):
    """Cnab regress contract data"""

    chave_contrato: Guid
    documento_titular: Document
    data_hora_criacao_contrato: CnabDateTime
    data_hora_vencimento_contrato: CnabDate
    data_assinatura_contrato: CnabDate
    efeito_contrato: EContractEffect
    metodo_divisao: EDivisionMethod
    tipo_garantia: EGuaranteeType
    valor_contrato: Money
    valor_garantia: Money
    percentual_valor_ur: int
    status_contrato: EContractStatus
    qt_unidade_recebivel: int
    identificacao_registro: ETransaction = ETransaction.CONTRACT_DATA

    def make_line(self):
        content = f"{self.identificacao_registro}{self.chave_contrato}{self.documento_titular}{self.data_hora_criacao_contrato}{self.data_hora_vencimento_contrato}{self.data_assinatura_contrato}{self.efeito_contrato}{self.metodo_divisao}{self.tipo_garantia}{self.valor_contrato}{self.valor_garantia}{self.percentual_valor_ur:03d}{self.status_contrato}{self.qt_unidade_recebivel:07d}"  # noqa: E501
        return f"{content}{make_spaces(400 - len(content))}"


@dataclass
class CnabReturnTypeTwo(ICnabLine):
    """Cnab regress data for liquidation"""

    chave_contrato: Guid
    banco: EBank | int | str
    agencia_conta: str
    numero_conta: str
    digito_conta: str
    tipo_conta: EAccountType
    tipo_documento_titular_conta: EDocumentType
    documento_titular_conta: Document
    identificacao_registro: ETransaction = ETransaction.BANK_LIQUIDATION_DATA

    def _generate_bank_code(self) -> str:
        if isinstance(self.banco, EBank):
            f_bank = str(self.banco)

        elif isinstance(self.banco, str):
            if len(self.banco) > 3:
                raise ValueError("Bank code should not be biger then 3 digits")

            f_bank = self.banco.zfill(3)

        elif isinstance(self.banco, int):
            if self.banco > 999:
                raise ValueError("Bank code should not be bigger then 999")

            f_bank = str(self.banco).zfill(3)

        return f"{f_bank}"

    def make_line(self):
        content = f"{self.identificacao_registro}{self.chave_contrato}{self._generate_bank_code()}{self.agencia_conta}{self.numero_conta}{self.digito_conta}{self.tipo_conta}{self.tipo_documento_titular_conta}{self.documento_titular_conta}"  # noqa: E501
        return f"{content}{make_spaces(400 - len(content))}"


@dataclass
class CnabReturnTypeThree(ICnabLine):
    """Cnab regress receivable unit data"""

    chave_contrato: Guid
    chave_unidade_recebivel: Guid
    tipo_documento_cedente: EDocumentType
    documento_cedente: Document
    documento_credenciadora: Document
    documento_titular: Document
    arranjo_pagamento: EArrangement
    data_liquidacao: CnabDate
    valor_unidade_recebivel: Money
    valor_comprometido_no_contrato: Money
    prioridade_contrato: int
    identificacao_registro: ETransaction = ETransaction.RECEIVABLES_UNIT_DATA

    def make_line(self):
        content = f"{self.identificacao_registro}{self.chave_contrato}{self.chave_unidade_recebivel}{self.tipo_documento_cedente}{self.documento_cedente}{self.documento_credenciadora}{self.documento_titular}{self.arranjo_pagamento}{self.data_liquidacao}{self.valor_unidade_recebivel}{self.valor_comprometido_no_contrato}{self.prioridade_contrato:03d}"  # noqa: E501
        return f"{content}{make_spaces(400 - len(content))}"
