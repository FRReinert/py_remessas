from unittest import TestCase

from faker import Faker

from cnab.cnab import CnabTrail


class TestCnabTrail(TestCase):
    def setUp(self):
        self.faker = Faker(locale='pt_BR')

    def test_cnab_trail_with_valid_data(self):
        trail = CnabTrail(20)
        self.assertEqual(trail.make_line()[:8], '90000020')
