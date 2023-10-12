import pytest
from io import StringIO
from cnab.interfaces import ICnabLine
from cnab.exporters import StreamSyncExporter


@pytest.fixture
def exporter():
    return StreamSyncExporter()


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
def iostream():
    return StringIO()


def test_export_single_contract(exporter, header_factory, trail_factory, contract_factory, iostream):
    contracts, expected_output = [contract_factory], "HEADER\nCONTRACT\nTRAIL\n"
    result = exporter.export(header_factory, trail_factory, contracts, iostream)
    assert result.getvalue() == expected_output


def test_export_multiple_contracts(exporter, header_factory, trail_factory, iostream):
    contracts, expected_output = [], "HEADER\nTRAIL\n"
    result = exporter.export(header_factory, trail_factory, contracts, iostream)
    assert result.getvalue() == expected_output


def test_export_edge_cases_large_number_of_contracts(exporter, header_factory, trail_factory, contract_factory, iostream):
    contracts, expected_output = [contract_factory] * 1000, "HEADER\n" + "CONTRACT\n" * 1000 + "TRAIL\n"
    result = exporter.export(header_factory, trail_factory, contracts, iostream)
    assert result.getvalue() == expected_output


def test_export_edge_cases_multiple_contracts(exporter, header_factory, trail_factory, contract_factory, iostream):
    contracts, expected_output = [contract_factory, contract_factory], "HEADER\nCONTRACT\nCONTRACT\nTRAIL\n"
    result = exporter.export(header_factory, trail_factory, contracts, iostream)
    assert result.getvalue() == expected_output


def test_export_edge_cases_single_contract(exporter, header_factory, trail_factory, contract_factory, iostream):
    contracts, expected_output = [contract_factory], "HEADER\nCONTRACT\nTRAIL\n"
    result = exporter.export(header_factory, trail_factory, contracts, iostream)
    assert result.getvalue() == expected_output


def test_export_no_header_factory(exporter, trail_factory, iostream):
    header_factory = None
    with pytest.raises(AttributeError):
        exporter.export(header_factory, trail_factory, iostream)


def test_export_no_trail_factory(exporter, header_factory, contract_factory, iostream):
    trail_factory = None
    with pytest.raises(AttributeError):
        exporter.export(header_factory, trail_factory, [contract_factory], iostream)


def test_export_no_contracts(exporter, header_factory, trail_factory, iostream):
    contracts = []
    result = exporter.export(header_factory, trail_factory, contracts, iostream)
    assert result.getvalue() == "HEADER\nTRAIL\n"


def test_export_no_iostream(exporter, header_factory, trail_factory, contract_factory):
    iostream = None
    result = exporter.export(header_factory, trail_factory, [contract_factory], iostream)
    assert result.getvalue() == "HEADER\nCONTRACT\nTRAIL\n"
