from uuid import uuid4

from cnab.regress import CnabName, CnabReturnTypeOne, CnabReturnTypeThree, CnabReturnHeader, CnabReturnTrail
from cnab.enums import (
    EArrangement,
    EContractEffect,
    EContractStatus,
    EDivisionMethod,
    EDocumentType,
    EGuaranteeType,
)
from cnab.exporters import FileExporter
from cnab.types import CnabDate, CnabDateTime, Document, Guid, Money

# properties
sequencial = 1
documento_cliente = Document("12345678901")

type1_return = {
    "chave_contrato": Guid(str(uuid4())),
    "documento_titular": Document("12345667801"),
    "data_hora_criacao_contrato": CnabDateTime(12, 12, 2023, 0, 0, 0),
    "data_hora_vencimento_contrato": CnabDate(12, 12, 2023),
    "data_assinatura_contrato": CnabDate(12, 12, 2023),
    "efeito_contrato": EContractEffect.GUARANTEE,
    "metodo_divisao": EDivisionMethod.NOMINAL_VALUE,
    "tipo_garantia": EGuaranteeType.FIDUCIARY,
    "valor_contrato": Money(1000),
    "valor_garantia": Money(1000),
    "percentual_valor_ur": 100,
    "status_contrato": EContractStatus.ACTIVE_REGISTRATION,
    "qt_unidade_recebivel": 1,
}

type3_return = {
    "chave_contrato": Guid(str(uuid4())),
    "chave_unidade_recebivel": Guid(str(uuid4())),
    "tipo_documento_cedente": EDocumentType.CPF,
    "documento_cedente": Document("12345678901"),
    "documento_credenciadora": Document("12345678901"),
    "documento_titular": Document("12345667801"),
    "arranjo_pagamento": EArrangement.AMEX_CREDIT_CARD,
    "data_liquidacao": CnabDate(12, 12, 2023),
    "valor_unidade_recebivel": Money(1000),
    "valor_comprometido_no_contrato": Money(1000),
    "prioridade_contrato": 1,
}

# contracts
contract_type_1 = CnabReturnTypeOne(**type1_return)
contract_type_3 = CnabReturnTypeThree(**type3_return)

# factories
cnab_name = CnabName('TR141000.RET', 'TR', 'RET', True)
cnab_head = CnabReturnHeader(sequencial, documento_cliente)
cnab_trail = CnabReturnTrail()

# exporter
exporter = FileExporter.export(cnab_name, cnab_head, cnab_trail, [contract_type_1, contract_type_3], './')
