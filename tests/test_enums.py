import unittest
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


class EnumTests(unittest.TestCase):
    def test_convertion_of_account_type_to_string(self):
        acc_one = EAccountType.CHECKING_ACCOUNT
        acc_two = EAccountType.DEPOSIT_ACCOUNT
        acc_thr = EAccountType.ESCROW_ACCOUNT
        acc_fou = EAccountType.INVESTMENT_ACCOUNT
        acc_fiv = EAccountType.PAYMENT_ACCOUNT
        acc_six = EAccountType.SAVINGS_ACCOUNT

        self.assertEqual(f"{acc_one}", 'CC')
        self.assertEqual(f"{acc_two}", 'CD')
        self.assertEqual(f"{acc_thr}", 'CG')
        self.assertEqual(f"{acc_fou}", 'CI')
        self.assertEqual(f"{acc_fiv}", 'PG')
        self.assertEqual(f"{acc_six}", 'PP')

    def test_convertion_of_document_to_string(self):
        doc_person = EDocumentType.CPF
        doc_company = EDocumentType.CNPJ

        self.assertEqual(f"{doc_person}", ' cpf')
        self.assertEqual(f"{doc_company}", 'cnpj')

    def test_string_convertion_contract_effect(self):
        eff_one = EContractEffect.TITULARITY_CHANGE
        eff_two = EContractEffect.GUARANTEE

        self.assertTrue(f"{eff_one}", "1")
        self.assertTrue(f"{eff_two}", "2")

    def test_string_convertion_division_method(self):
        div_one = EDivisionMethod.NOMINAL_VALUE
        div_two = EDivisionMethod.PERCENTAGE

        self.assertEqual(f"{div_one}", "1")
        self.assertEqual(f"{div_two}", "2")

    def test_string_conversion_guarantee_type(self):
        gua_one = EGuaranteeType.NO_GUARRANTEE
        gua_two = EGuaranteeType.FIDUCIARY
        gua_thr = EGuaranteeType.PLEDGE
        gua_fou = EGuaranteeType.PROMISE_TO_PAY

        self.assertEqual(f"{gua_one}", "0")
        self.assertEqual(f"{gua_two}", "1")
        self.assertEqual(f"{gua_thr}", "2")
        self.assertEqual(f"{gua_fou}", "3")

    def test_string_convertion_contract_status(self):
        contract_status_one = EContractStatus.PENDING_REGISTRATION
        contract_status_two = EContractStatus.ACTIVE_REGISTRATION
        contract_status_thr = EContractStatus.CANCELLED_REGISTRATION
        contract_status_fou = EContractStatus.UNABLE_TO_REGSTER

        self.assertEqual(f"{contract_status_one}", "1")
        self.assertEqual(f"{contract_status_two}", "2")
        self.assertEqual(f"{contract_status_thr}", "3")
        self.assertEqual(f"{contract_status_fou}", "4")

    def test_string_conversion_transaction(self):
        trans_one = ETransaction.CONTRACT_DATA
        trans_two = ETransaction.BANK_LIQUIDATION_DATA
        trans_thr = ETransaction.RECEIVABLES_UNIT_DATA

        self.assertTrue(f"{trans_one}", "1")
        self.assertTrue(f"{trans_two}", "2")
        self.assertTrue(f"{trans_thr}", "3")

    def test_string_convertion_arrangement(self):
        self.assertEqual(f"{EArrangement.AMEX_CREDIT_CARD}", 'ACC')
        self.assertEqual(f"{EArrangement.BANESCARD_CREDIT_CARD}", 'BBC')
        self.assertEqual(f"{EArrangement.BANESCARD_DEBIT_CARD}", 'BCD')
        self.assertEqual(f"{EArrangement.BEN_VISA_VALE}", 'BVV')
        self.assertEqual(f"{EArrangement.CIELO_AMEX_CREDT}", 'CAC')
        self.assertEqual(f"{EArrangement.CABAL_CREDIT}", 'CBC')
        self.assertEqual(f"{EArrangement.CABAL_DEBIT}", 'CBD')
        self.assertEqual(f"{EArrangement.CABAL_PRE_PAID}", 'CBP')
        self.assertEqual(f"{EArrangement.CIELO_DINERS_CREDIT_CARD}", 'CDC')
        self.assertEqual(f"{EArrangement.CIELO_ELO_CREDIT_CARD}", 'CEC')
        self.assertEqual(f"{EArrangement.CIELO_ELO_DEBIT_CARD}", 'CED')
        self.assertEqual(f"{EArrangement.CIELO_HIPERCARD_CREDIT}", 'CHC')
        self.assertEqual(f"{EArrangement.CIELO_MASTERCARD_CREDIT}", 'CMC')
        self.assertEqual(f"{EArrangement.CIELO_MASTERCARD_DEBIT}", 'CMD')
        self.assertEqual(f"{EArrangement.CREDZ_CREDIT}", 'CZC')
        self.assertEqual(f"{EArrangement.DINERS_DEBIT_CARD}", 'DCC')
        self.assertEqual(f"{EArrangement.ELO_CREDIT_CARD}", 'ECC')
        self.assertEqual(f"{EArrangement.ELO_DEBIT_CARD}", 'ECD')
        self.assertEqual(f"{EArrangement.GOODCARD_CREDIT}", 'GCC')
        self.assertEqual(f"{EArrangement.GLOBAL_PAYMENTS_DINERS_CREDIT}", 'GDC')
        self.assertEqual(f"{EArrangement.GLOBAL_PAYMENTS_MASTERCARD_CREDIT}", 'GMC')
        self.assertEqual(f"{EArrangement.GLOBAL_PAYMENTS_MASTERCARD_DEBIT}", 'GMD')
        self.assertEqual(f"{EArrangement.GLOBAL_PAYMENTS_VISA_CREDIT}", 'GVC')
        self.assertEqual(f"{EArrangement.GLOBAL_PAYMENTS_VISA_DEBIT}", 'GVD')
        self.assertEqual(f"{EArrangement.HIPERCARD_CREDIT_CARD}", 'HCC')
        self.assertEqual(f"{EArrangement.JCB_CREDIT_CARD}", 'JCC')
        self.assertEqual(f"{EArrangement.MAIS_CREDIT_CARD}", 'MAC')
        self.assertEqual(f"{EArrangement.MASTERCARD_ATM_CARD}", 'MCA')
        self.assertEqual(f"{EArrangement.MASTERCARD_CREDIT_CARD}", 'MCC')
        self.assertEqual(f"{EArrangement.MASTERCARD_DEBIT_CARD}", 'MCD')
        self.assertEqual(f"{EArrangement.MASTERCARD_PREPAYD_CARD}", 'MCP')
        self.assertEqual(f"{EArrangement.OUROCARD_DEBIT_CARD}", 'OCD')
        self.assertEqual(f"{EArrangement.SOROCRED_CREDIT_CARD}", 'SCC')
        self.assertEqual(f"{EArrangement.SOROCRED_DEBIT_CARD}", 'SCD')
        self.assertEqual(f"{EArrangement.VISA_ATM_CARD}", 'VCA')
        self.assertEqual(f"{EArrangement.VISA_CREDIT_CARD}", 'VCC')
        self.assertEqual(f"{EArrangement.VISA_DEBIT_CARD}", 'VCD')
        self.assertEqual(f"{EArrangement.VISA_PREPAID_CARD}", 'VCP')
        self.assertEqual(f"{EArrangement.VERDECARD_CREDIT_CARD}", 'VDC')
        self.assertEqual(f"{EArrangement.VISA_INTERNATIONAL_PURCHASE_CREDIT}", 'VIC')
        self.assertEqual(f"{EArrangement.VISA_INTERNATIONAL_PURCHASE_DEBIT}", 'VID')

    def test_string_convertion_brz_banks(self):
        self.assertTrue(f"{EBank.STONE_PAGAMENTOS}", "197")
        self.assertTrue(f"{EBank.BANCO_COOPERATIVO_SICREDI_SA}", "748")
        self.assertTrue(f"{EBank.ADVANCED_CC_LTDA}", "117")
        self.assertTrue(f"{EBank.BANCO_INTER}", "077")
        self.assertTrue(f"{EBank.NEON_PAGAMENTOS}", "735")
        self.assertTrue(f"{EBank.SUPERDIGITAL}", "340")
        self.assertTrue(f"{EBank.PAGBANK}", "290")
        self.assertTrue(f"{EBank.BANCO_AGIBANK_SA}", "121")
        self.assertTrue(f"{EBank.NEXT}", "237")
        self.assertTrue(f"{EBank.BANCO_ORIGINAL}", "212")
        self.assertTrue(f"{EBank.NUBANK}", "260")
        self.assertTrue(f"{EBank.BANCO_WILLBANK}", "280")
        self.assertTrue(f"{EBank.ALBATROSS_CCV_SA}", "172")
        self.assertTrue(f"{EBank.MERCADO_PAGO}", "323")
        self.assertTrue(f"{EBank.ATIVA_INVESTIMENTOS_SA}", "188")
        self.assertTrue(f"{EBank.PICPAY}", "380")
        self.assertTrue(f"{EBank.AVISTA_SA_CRÉDITO_FINANCIAMENTO_E_INVESTIMENTO}", "280")  # noqa: E501
        self.assertTrue(f"{EBank.B_T_CC_LTDA}", "080")
        self.assertTrue(f"{EBank.BANCO_AJR_ENNER_SA}", "654")
        self.assertTrue(f"{EBank.BANCO_ABC_BRASIL_SA}", "246")
        self.assertTrue(f"{EBank.BANCO_ABN_AMRO_SA}", "075")
        self.assertTrue(f"{EBank.BANCO_AGIBANK_BRASIL_SA}", "121")
        self.assertTrue(f"{EBank.BANCO_ALFA_SA}", "025")
        self.assertTrue(f"{EBank.BANCO_ALVORADA_SA}", "641")
        self.assertTrue(f"{EBank.BANCO_ANDBANK_BRASIL_SA}", "065")
        self.assertTrue(f"{EBank.BANCO_ARBI_SA}", "213")
        self.assertTrue(f"{EBank.BANCO_B3_SA}", "096")
        self.assertTrue(f"{EBank.BANCO_SANTANDER}", "033")
        self.assertTrue(f"{EBank.BANCO_BMG_SA}", "318")
        self.assertTrue(f"{EBank.BANCO_BNP_PARIBAS_BRASIL_SA}", "752")
        self.assertTrue(f"{EBank.BANCO_BOCOM_BBM_SA}", "107")
        self.assertTrue(f"{EBank.BANCO_BRADESCARD_SA}", "063")
        self.assertTrue(f"{EBank.CÓDIGO_BANCO_BEG_SA}", "031")
        self.assertTrue(f"{EBank.BANCO_BRADESCO_BERJ_SA}", "122")
        self.assertTrue(f"{EBank.BANCO_BRADESCO_CARTÕES_SA}", "204")
        self.assertTrue(f"{EBank.BANCO_BRADESCO_FINANCIAMENTOS_SA}", "394")
        self.assertTrue(f"{EBank.BANCO_BRADESCO_SA}", "237")
        self.assertTrue(f"{EBank.BANCO_BS2_SA}", "218")
        self.assertTrue(f"{EBank.BANCO_BTG_PACTUAL_SA}", "208")
        self.assertTrue(f"{EBank.BANCO_C6_SA_C6_BANK}", "336")
        self.assertTrue(f"{EBank.BANCO_CAIXA_GERAL_BRASIL_SA}", "473")
        self.assertTrue(f"{EBank.BANCO_CAIXA_ECONÔMICA_FEDERAL}", "104")
        self.assertTrue(f"{EBank.BANCO_CAPITAL_SA}", "412")
        self.assertTrue(f"{EBank.BANCO_CARGILL_SA}", "040")
        self.assertTrue(f"{EBank.BANCO_CARREFOUR}", "368")
        self.assertTrue(f"{EBank.BANCO_CÉDULA_SA}", "266")
        self.assertTrue(f"{EBank.BANCO_CETELEM_SA}", "739")
        self.assertTrue(f"{EBank.BANCO_CIFRA_SA}", "233")
        self.assertTrue(f"{EBank.BANCO_CITIBANK_SA}", "745")
        self.assertTrue(f"{EBank.BANCO_CLÁSSICO_SA}", "241")
        self.assertTrue(f"{EBank.BANCO_COOPERATIVO_DO_BRASIL_SA_BANCOOB}", "756")
        self.assertTrue(f"{EBank.BANCO_CREDIT_AGRICOLE_BRASIL_SA}", "222")
        self.assertTrue(f"{EBank.BANCO_CREDIT_SUISSE_BRASIL_SA}", "505")
        self.assertTrue(f"{EBank.BANCO_CREFISA_SA}", "069")
        self.assertTrue(f"{EBank.BANCO_DA_AMAZÔNIA_SA}", "003")
        self.assertTrue(f"{EBank.BANCO_DA_CHINA_BRASIL_SA}", "083")
        self.assertTrue(f"{EBank.BANCO_DAYCOVAL_SA}", "707")
        self.assertTrue(f"{EBank.BANCO_DE_DESENVOLVIMENTO_DO_ESPIRITO_SANTO_SA}", "051")
        self.assertTrue(f"{EBank.BANCO_DE_LA_NACION_ARGENTINA}", "300")
        self.assertTrue(f"{EBank.BANCO_DE_LA_PROVINCIA_DE_BUENOS_AIRES}", "495")
        self.assertTrue(f"{EBank.BANCO_DE_LA_REPUBLICA_ORIENTAL_DEL_URUGUAY}", "494")
        self.assertTrue(f"{EBank.BANCO_DIGIO_SA}", "335")
        self.assertTrue(f"{EBank.BANCO_DO_BRASIL_SA}", "001")
        self.assertTrue(f"{EBank.BANCO_DO_ESTADO_DE_SERGIPE_SA}", "047")
        self.assertTrue(f"{EBank.BANCO_DO_ESTADO_DO_PARA_SA}", "037")
        self.assertTrue(f"{EBank.BANCO_DO_ESTADO_DO_RIO_GRANDE_DO_SUL_SA}", "041")
        self.assertTrue(f"{EBank.BANCO_DO_NORDESTE_DO_BRASIL_SA}", "004")
        self.assertTrue(f"{EBank.BANCO_FAIR_CORRETORA_DE_CÂMBIO_SA}", "196")
        self.assertTrue(f"{EBank.BANCO_FATOR_SA}", "265")
        self.assertTrue(f"{EBank.BANCO_FIBRA_SA}", "224")
        self.assertTrue(f"{EBank.BANCO_FICSA_SA}", "626")
        self.assertTrue(f"{EBank.BANCO_FINAXIS_SA}", "094")
        self.assertTrue(f"{EBank.BANCO_GUANABARA_SA}", "612")
        self.assertTrue(f"{EBank.BANCO_INBURSA_SA}", "012")
        self.assertTrue(f"{EBank.BANCO_INDUSTRIAL_DO_BRASIL_SA}", "604")
        self.assertTrue(f"{EBank.BANCO_INDUSVAL_SA}", "653")
        self.assertTrue(f"{EBank.BANCO_INTER_SA}", "077")
        self.assertTrue(f"{EBank.BANCO_INVESTCRED_UNIBANCO_SA}", "249")
        self.assertTrue(f"{EBank.BANCO_ITAÚ_BBA_SA}", "184")
        self.assertTrue(f"{EBank.BANCO_ITAÚ_CONSIGNADO_SA}", "029")
        self.assertTrue(f"{EBank.BANCO_ITAUBANK_SA}", "479")
        self.assertTrue(f"{EBank.BANCO_ITAÚ}", "341")
        self.assertTrue(f"{EBank.BANCO_JP_MORGAN_SA}", "376")
        self.assertTrue(f"{EBank.BANCO_SAFRA}", "422")
        self.assertTrue(f"{EBank.BANCO_JOHN_DEERE_SA}", "217")
        self.assertTrue(f"{EBank.BANCO_KDB_SA}", "076")
        self.assertTrue(f"{EBank.BANCO_KEB_HANA_DO_BRASIL_SA}", "757")
        self.assertTrue(f"{EBank.BANCO_LUSO_BRASILEIRO_SA}", "600")
        self.assertTrue(f"{EBank.BANCO_MÁXIMA_SA}", "243")
        self.assertTrue(f"{EBank.BANCO_MAXINVEST_SA}", "720")
        self.assertTrue(f"{EBank.BANCO_MERCANTIL_DO_BRASIL_SA}", "389")
        self.assertTrue(f"{EBank.BANCO_MIZUHO_DO_BRASIL_SA}", "370")
        self.assertTrue(f"{EBank.BANCO_MODAL_SA}", "746")
        self.assertTrue(f"{EBank.BANCO_MORGAN_STANLEY_SA}", "066")
        self.assertTrue(f"{EBank.BANCO_MUFG_BRASIL_SA}", "456")
        self.assertTrue(f"{EBank.BANCO_NACIONAL_DE_DESENVOLVIMENTO_ECONÔMICO_E_SOCIAL_BNDES}", "007",)  # noqa: E501
