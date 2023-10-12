import unittest
from unittest.mock import mock_open, patch
import pytest
from cnab.interfaces import ICnabLine
from cnab.exporters import FileExporter


@pytest.fixture
def name_factory():
    class MockNameFactory:
        def make_name(self):
            return "mockname.RET"

    return MockNameFactory()


@pytest.fixture
def header_factory():
    class MockHeaderFactory(ICnabLine):
        def make_line(self):
            return "HEADER"

    return MockHeaderFactory()


@pytest.fixture
def trail_factory():
    class MockTrailFactory(ICnabLine):
        def make_line(self):
            return "TRAIL"

    return MockTrailFactory()


@pytest.fixture
def contract_factory():
    class MockContractFactory(ICnabLine):
        def make_line(self):
            return "CONTRACT"

    return MockContractFactory()


@pytest.fixture
def file_path(tmp_path):
    return str(tmp_path / "test_file.txt")


def test_export_with_valid_data(
    name_factory, header_factory, trail_factory, contract_factory, file_path
):
    contracts = [contract_factory, contract_factory, contract_factory]

    mock = mock_open()
    with patch('builtins.open', mock):
        FileExporter.export(
            name_factory, header_factory, trail_factory, contracts, file_path
        )

    mock().write.assert_any_call('HEADER\n')
    mock().write.assert_any_call('CONTRACT\n')
    mock().write.assert_any_call('TRAIL\n')


def test_export_with_empty_contracts(
    name_factory, header_factory, trail_factory, file_path
):
    contracts = []
    mock = mock_open()
    with patch('builtins.open', mock):
        FileExporter.export(
            name_factory, header_factory, trail_factory, contracts, file_path
        )

    mock().write.assert_any_call('HEADER\n')
    mock().write.assert_any_call('TRAIL\n')
