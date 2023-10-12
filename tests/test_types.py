from unittest import TestCase
from uuid import uuid4

from faker import Faker

from cnab.types import CnabDate, CnabDateTime, Document, Guid, Money


class TestCnabTypes(TestCase):
    def setUp(self):
        self.faker = Faker(locale='pt_BR')

    def test_cnab_date_conversion_to_string(self):
        date = CnabDate(1, 1, 2020)
        self.assertEqual(f"{date}", "2020-01-01")

    def test_cnab_date_time_conversion_to_string(self):
        dtime = CnabDateTime(12, 12, 2000, 13, 22, 40)
        self.assertEqual(f"{dtime}", "2000-12-12 13:22:40")

    def test_guid_to_string(self):
        uid = str(uuid4())
        guid = Guid(uid)
        self.assertEqual(f"{guid}", uid)

    def test_guid_is_valid(self):
        uid4 = str(uuid4())
        fake_uid = "123123123-1231232321-1231231231"

        guid4 = Guid(uid4)
        self.assertTrue(guid4.is_valid())

        fake_guid = Guid(fake_uid)
        self.assertFalse(fake_guid.is_valid())

    def test_money_to_string_conversion(self):
        val_1 = Money(220)
        val_2 = Money(15534390)
        val_3 = Money(20000.15)
        val_4 = Money(35.1432)
        val_5 = Money(35_825.1432)
        self.assertEqual(f"{val_1}", "000000000000220")
        self.assertEqual(f"{val_2}", "000000015534390")
        self.assertEqual(f"{val_3}", "000000002000015")
        self.assertEqual(f"{val_4}", "000000000003514")
        self.assertEqual(f"{val_5}", "000000003582514")

    def test_document_conversion_to_string(self):
        personal_inst = Document("923.273.240-84")
        company_inst = Document("50.048.319/0001-65")

        self.assertEqual(f"{personal_inst}", "00092327324084")
        self.assertEqual(f"{company_inst}", "50048319000165")
