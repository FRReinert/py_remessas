from enum import Enum


class EFineType(str, Enum):
    WITH_FINE = "2"
    WITHOUT_FINE = "0"

    def __str__(self):
        return self.value


class EReceivableType(str, Enum):
    DUPLICATE = "01"
    PROMISSORY_NOTE = "02"
    INSURANCE_NOTE = "03"
    RECEIPT = "05"
    BILLS_OF_EXCHANGE = "10"
    DEBIT_NOTE = "11"
    SERVICE_DUPLICATE = "12"
    CREDIT_CARD = "31"
    PROPOSAL_SLIP = "32"
    DEPOSIT_AND_CONTRIBUTION = "33"
    OTHERS = "99"

    def __str__(self):
        return self.value


class EConditionForSlipEmission(str, Enum):
    BANK_ISSUE_AND_PROCESS = 1
    CUSTOMER_ISSUE_AND_BANK_PROCESS = 2

    def __str__(self):
        return self.value


class EAccountType(str, Enum):
    CHECKING_ACCOUNT = 'CC'
    DEPOSIT_ACCOUNT = 'CD'
    ESCROW_ACCOUNT = 'CG'
    PAYMENT_ACCOUNT = 'PG'
    SAVINGS_ACCOUNT = 'PP'
    INVESTMENT_ACCOUNT = 'CI'

    def __str__(self):
        return self.value


class EDocumentType(str, Enum):
    CPF = ' CPF'
    CNPJ = 'CNPJ'

    def __str__(self):
        return self.value


class EContractEffect(int, Enum):
    TITULARITY_CHANGE = 1
    GUARANTEE = 2

    def __str__(self):
        return f"{self.value}"


class EDivisionMethod(int, Enum):
    NOMINAL_VALUE = 1
    PERCENTAGE = 2

    def __str__(self):
        return f"{self.value}"


class EGuaranteeType(int, Enum):
    NO_GUARRANTEE = 0
    FIDUCIARY = 1
    PLEDGE = 2
    PROMISE_TO_PAY = 3

    def __str__(self):
        return f"{self.value}"


class EContractStatus(int, Enum):
    PENDING_REGISTRATION = 1
    ACTIVE_REGISTRATION = 2
    CANCELLED_REGISTRATION = 3
    UNABLE_TO_REGSTER = 4

    def __str__(self):
        return f"{self.value}"


class ETransaction(int, Enum):
    CONTRACT_DATA = 1
    BANK_LIQUIDATION_DATA = 2
    RECEIVABLES_UNIT_DATA = 3

    def __str__(self):
        return f"{self.value}"


class EArrangement(str, Enum):
    AMEX_CREDIT_CARD = 'ACC'
    BANESCARD_CREDIT_CARD = 'BBC'
    BANESCARD_DEBIT_CARD = 'BCD'
    BEN_VISA_VALE = 'BVV'
    CIELO_AMEX_CREDT = 'CAC'
    CABAL_CREDIT = 'CBC'
    CABAL_DEBIT = 'CBD'
    CABAL_PRE_PAID = 'CBP'
    CIELO_DINERS_CREDIT_CARD = 'CDC'
    CIELO_ELO_CREDIT_CARD = 'CEC'
    CIELO_ELO_DEBIT_CARD = 'CED'
    CIELO_HIPERCARD_CREDIT = 'CHC'
    CIELO_MASTERCARD_CREDIT = 'CMC'
    CIELO_MASTERCARD_DEBIT = 'CMD'
    CREDZ_CREDIT = 'CZC'
    DINERS_DEBIT_CARD = 'DCC'
    ELO_CREDIT_CARD = 'ECC'
    ELO_DEBIT_CARD = 'ECD'
    GOODCARD_CREDIT = 'GCC'
    GLOBAL_PAYMENTS_DINERS_CREDIT = 'GDC'
    GLOBAL_PAYMENTS_MASTERCARD_CREDIT = 'GMC'
    GLOBAL_PAYMENTS_MASTERCARD_DEBIT = 'GMD'
    GLOBAL_PAYMENTS_VISA_CREDIT = 'GVC'
    GLOBAL_PAYMENTS_VISA_DEBIT = 'GVD'
    HIPERCARD_CREDIT_CARD = 'HCC'
    JCB_CREDIT_CARD = 'JCC'
    MAIS_CREDIT_CARD = 'MAC'
    MASTERCARD_ATM_CARD = 'MCA'
    MASTERCARD_CREDIT_CARD = 'MCC'
    MASTERCARD_DEBIT_CARD = 'MCD'
    MASTERCARD_PREPAYD_CARD = 'MCP'
    OUROCARD_DEBIT_CARD = 'OCD'
    SOROCRED_CREDIT_CARD = 'SCC'
    SOROCRED_DEBIT_CARD = 'SCD'
    VISA_ATM_CARD = 'VCA'
    VISA_CREDIT_CARD = 'VCC'
    VISA_DEBIT_CARD = 'VCD'
    VISA_PREPAID_CARD = 'VCP'
    VERDECARD_CREDIT_CARD = 'VDC'
    VISA_INTERNATIONAL_PURCHASE_CREDIT = 'VIC'
    VISA_INTERNATIONAL_PURCHASE_DEBIT = 'VID'

    def __str__(self):
        return f"{self.value}"


class EBank(int, Enum):
    ADVANCED_CC_LTDA = 117
    ALBATROSS_CCV_SA = 172
    ATIVA_INVESTIMENTOS_SA = 188
    AVISTA_SA_CRÉDITO_FINANCIAMENTO_E_INVESTIMENTO = 280
    B_T_CC_LTDA = 80
    BANCO_ABC_BRASIL_SA = 246
    BANCO_ABN_AMRO_SA = 75
    BANCO_AGIBANK_BRASIL_SA = 121
    BANCO_AGIBANK_SA = 121
    BANCO_AJR_ENNER_SA = 654
    BANCO_ALFA_SA = 25
    BANCO_ALVORADA_SA = 641
    BANCO_ANDBANK_BRASIL_SA = 65
    BANCO_ARBI_SA = 213
    BANCO_B3_SA = 96
    BANCO_BMG_SA = 318
    BANCO_BNP_PARIBAS_BRASIL_SA = 752
    BANCO_BOCOM_BBM_SA = 107
    BANCO_BRADESCARD_SA = 63
    BANCO_BRADESCO_BERJ_SA = 122
    BANCO_BRADESCO_CARTÕES_SA = 204
    BANCO_BRADESCO_FINANCIAMENTOS_SA = 394
    BANCO_BRADESCO_SA = 237
    BANCO_BS2_SA = 218
    BANCO_BTG_PACTUAL_SA = 208
    BANCO_C6_SA_C6_BANK = 336
    BANCO_CAIXA_ECONÔMICA_FEDERAL = 104
    BANCO_CAIXA_GERAL_BRASIL_SA = 473
    BANCO_CAPITAL_SA = 412
    BANCO_CARGILL_SA = 40
    BANCO_CARREFOUR = 368
    BANCO_CÉDULA_SA = 266
    BANCO_CETELEM_SA = 739
    BANCO_CIFRA_SA = 233
    BANCO_CITIBANK_SA = 745
    BANCO_CLÁSSICO_SA = 241
    BANCO_COOPERATIVO_DO_BRASIL_SA_BANCOOB = 756
    BANCO_COOPERATIVO_SICREDI_SA = 748
    BANCO_CREDIT_AGRICOLE_BRASIL_SA = 222
    BANCO_CREDIT_SUISSE_BRASIL_SA = 505
    BANCO_CREFISA_SA = 69
    BANCO_DA_AMAZÔNIA_SA = 3
    BANCO_DA_CHINA_BRASIL_SA = 83
    BANCO_DAYCOVAL_SA = 707
    BANCO_DE_DESENVOLVIMENTO_DO_ESPIRITO_SANTO_SA = 51
    BANCO_DE_LA_NACION_ARGENTINA = 300
    BANCO_DE_LA_PROVINCIA_DE_BUENOS_AIRES = 495
    BANCO_DE_LA_REPUBLICA_ORIENTAL_DEL_URUGUAY = 494
    BANCO_DIGIO_SA = 335
    BANCO_DO_BRASIL_SA = 1
    BANCO_DO_ESTADO_DE_SERGIPE_SA = 47
    BANCO_DO_ESTADO_DO_PARA_SA = 37
    BANCO_DO_ESTADO_DO_RIO_GRANDE_DO_SUL_SA = 41
    BANCO_DO_NORDESTE_DO_BRASIL_SA = 4
    BANCO_FAIR_CORRETORA_DE_CÂMBIO_SA = 196
    BANCO_FATOR_SA = 265
    BANCO_FIBRA_SA = 224
    BANCO_FICSA_SA = 626
    BANCO_FINAXIS_SA = 94
    BANCO_GUANABARA_SA = 612
    BANCO_INBURSA_SA = 12
    BANCO_INDUSTRIAL_DO_BRASIL_SA = 604
    BANCO_INDUSVAL_SA = 653
    BANCO_INTER = 77
    BANCO_INTER_SA = 77
    BANCO_INVESTCRED_UNIBANCO_SA = 249
    BANCO_ITAÚ = 341
    BANCO_ITAÚ_BBA_SA = 184
    BANCO_ITAÚ_CONSIGNADO_SA = 29
    BANCO_ITAUBANK_SA = 479
    BANCO_JOHN_DEERE_SA = 217
    BANCO_JP_MORGAN_SA = 376
    BANCO_KDB_SA = 76
    BANCO_KEB_HANA_DO_BRASIL_SA = 757
    BANCO_LUSO_BRASILEIRO_SA = 600
    BANCO_MÁXIMA_SA = 243
    BANCO_MAXINVEST_SA = 720
    BANCO_MERCANTIL_DO_BRASIL_SA = 389
    BANCO_MIZUHO_DO_BRASIL_SA = 370
    BANCO_MODAL_SA = 746
    BANCO_MORGAN_STANLEY_SA = 66
    BANCO_MUFG_BRASIL_SA = 456
    BANCO_NACIONAL_DE_DESENVOLVIMENTO_ECONÔMICO_E_SOCIAL_BNDES = 7
    BANCO_ORIGINAL = 212
    BANCO_SAFRA = 422
    BANCO_SANTANDER = 33
    BANCO_WILLBANK = 280
    CÓDIGO_BANCO_BEG_SA = 31
    MERCADO_PAGO = 323
    NEON_PAGAMENTOS = 735
    NUBANK = 260
    PAGBANK = 290
    PICPAY = 380
    STONE_PAGAMENTOS = 197
    SUPERDIGITAL = 340

    def __str__(self):
        return f"{self.value:03d}"

    def bank_name(self, length: int) -> str:
        content: str
        match self.value:
            case 197:
                content = "STONE"
            case 748:
                content = "SICREDI"
            case 117:
                content = "ADVANCED"
            case 77:
                content = "INTER"
            case 735:
                content = "NU PAGAMENTOS"
            case 340:
                content = "SUPERDIGITAL"
            case 290:
                content = "PAGBANK"
            case 121:
                content = "AGIBANKE"
            case 212:
                content = "ORIGINAL"
            case 260:
                content = "NUBANK"
            case 280:
                content = "WILLBANK"
            case 172:
                content = "ALBATROSS"
            case 323:
                content = "MERCADO PAGO"
            case 188:
                content = "ATIVA"
            case 380:
                content = "PICPAY"
            case 280:
                content = "ANVISTA"
            case 80:
                content = "BET"
            case 654:
                content = "AJR ENNER"
            case 246:
                content = "ABC BRASIL"
            case 75:
                content = "ABN AMRO"
            case 121:
                content = "AGIBANK"
            case 25:
                content = "ALFA"
            case 641:
                content = "ALVORADA"
            case 65:
                content = "ANDBANK"
            case 213:
                content = "ARBI"
            case 96:
                content = "B3"
            case 33:
                content = "SANTANDER"
            case 318:
                content = "BMG"
            case 752:
                content = "BNP PARIBAS"
            case 107:
                content = "BOCOM BBM"
            case 63:
                content = "BRADESCARD"
            case 31:
                content = "CÓDIGO BEG"
            case 122:
                content = "BRADESCO BERJ"
            case 204:
                content = "BRADESCO CART"
            case 394:
                content = "BRADESCO FIN"
            case 237:
                content = "BRADESCO"
            case 218:
                content = "BS2"
            case 208:
                content = "BTG PACTUAL"
            case 336:
                content = "C6 BANK"
            case 473:
                content = "CAIXA GERAL"
            case 104:
                content = "CAIXA"
            case 412:
                content = "CAPITAL"
            case 40:
                content = "CARGILL"
            case 368:
                content = "CARREFOUR"
            case 266:
                content = "CÉDULA"
            case 739:
                content = "CETELEM"
            case 233:
                content = "CIFRA"
            case 745:
                content = "CITIBANK"
            case 241:
                content = "CLÁSSICO"
            case 756:
                content = "BANCOOB"
            case 222:
                content = "CREDIT AGRICOLE"
            case 505:
                content = "CREDIT SUISSE"
            case 69:
                content = "CREFISA"
            case 3:
                content = "BANCO AMAZONIA"
            case 83:
                content = "BANCO DA CHINA"
            case 707:
                content = "DAYCOVAL"
            case 51:
                content = "ESPIRITO STO"
            case 300:
                content = "BANCO ARGENTINA"
            case 495:
                content = "BANCO BUENOS AI"
            case 494:
                content = "BANCO URUGUAY"
            case 335:
                content = "DIGIO"
            case 1:
                content = "BANCO DO BRASIL"
            case 47:
                content = "BANCO SERGIPE"
            case 37:
                content = "BANCO PARA"
            case 41:
                content = "BANCO RS"
            case 4:
                content = "BANCO NE"
            case 196:
                content = "FAIR"
            case 265:
                content = "FATOR"
            case 224:
                content = "FIBRA"
            case 626:
                content = "FICSA"
            case 94:
                content = "FINAXIS"
            case 612:
                content = "GUANABARA"
            case 12:
                content = "INBURSA"
            case 604:
                content = "BANCO INDUSTRIA"
            case 653:
                content = "INDUSVAL"
            case 77:
                content = "INTER"
            case 249:
                content = "INVESTCRED"
            case 184:
                content = "ITAU BBA"
            case 29:
                content = "ITAU CONSIGNADO"
            case 479:
                content = "ITAUBANK"
            case 341:
                content = "ITAU"
            case 376:
                content = "JP MORGAN"
            case 422:
                content = "BANCOFRA"
            case 217:
                content = "JOHN DEERE"
            case 76:
                content = "KDB"
            case 757:
                content = "KEB HANA"
            case 600:
                content = "LUSO BRASILEIRO"
            case 243:
                content = "MAXIMA"
            case 720:
                content = "MAXINVEST"
            case 389:
                content = "MERCANTIL"
            case 370:
                content = "MIZUHO BRASIL"
            case 746:
                content = "MODAL"
            case 66:
                content = "MORGAN STANLEY"
            case 456:
                content = "MUFG BRASIL"
            case 7:
                content = "BNDES"
            case _:
                content = ""
        return content.ljust(length + 1)[:length]
