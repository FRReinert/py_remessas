from unittest import TestCase

from faker import Faker

from cnab.regress import CnabReturnHeader
from cnab.types import Document


class TestCnabReturnHeaders(TestCase):
    def setUp(self) -> None:
        self.faker = Faker('pt_BR')

    def test_cnab_header_with_valid_data(self):
        personal_doc: str = Document("923.273.240-84")
        company_doc: str = Document("80.068.450/0001-55")

        personal_header = CnabReturnHeader(customer_document=personal_doc, unique_id=1)
        company_header = CnabReturnHeader(customer_document=company_doc, unique_id=2)

        personal_line = '02RETORNO00000011CONTRATO00092327324084'
        company_line = '02RETORNO00000021CONTRATO80068450000155'

        self.assertEqual(personal_header.make_line()[:39], personal_line)
        self.assertEqual(company_header.make_line()[:39], company_line)
