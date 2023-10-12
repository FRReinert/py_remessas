import pytest
from cnab.interfaces import ICnabLine
from cnab.exporters import GeneratorExporter


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
def exporter(header_factory, trail_factory):
    return GeneratorExporter()


def test_export_happy_path_no_contracts(
    exporter,
    header_factory,
    trail_factory,
):
    contracts, expected_output = [], ["HEADER", "TRAIL"]
    assert (
        list(exporter.export(header_factory, trail_factory, contracts))
        == expected_output
    )


def test_export_happy_path_one_contract(
    exporter,
    header_factory,
    trail_factory,
    contract_factory,
):
    contracts, expected_output = [contract_factory], [
        "HEADER",
        "CONTRACT",
        "TRAIL",
    ]
    assert (
        list(exporter.export(header_factory, trail_factory, contracts))
        == expected_output
    )


def test_export_happy_path_multiple_contracts(
    exporter,
    header_factory,
    trail_factory,
    contract_factory,
):
    contracts, expected_output = [contract_factory, contract_factory], [
        "HEADER",
        "CONTRACT",
        "CONTRACT",
        "TRAIL",
    ]
    assert (
        list(exporter.export(header_factory, trail_factory, contracts))
        == expected_output
    )


def test_export_edge_cases_no_contracts(
    exporter,
    header_factory,
    trail_factory,
):

    contracts, expected_output = [], ["HEADER", "TRAIL"]
    assert (list(exporter.export(header_factory, trail_factory, contracts)) == expected_output)


def test_export_edge_cases_single_contract(
    exporter,
    header_factory,
    trail_factory,
    contract_factory,
):
    contracts, expected_output = [contract_factory], ["HEADER", "CONTRACT", "TRAIL"]
    assert (list(exporter.export(header_factory, trail_factory, contracts)) == expected_output)


def test_export_edge_cases_multiple_contracts(
    exporter,
    header_factory,
    trail_factory,
    contract_factory,
):
    contracts, expected_output = [contract_factory, contract_factory], ["HEADER", "CONTRACT", "CONTRACT", "TRAIL"],
    assert (list(exporter.export(header_factory, trail_factory, contracts)) == expected_output)


def test_export_error_cases_multiple_contracts(
    exporter,
    header_factory,
    trail_factory,
    contract_factory,
):
    contracts, expected_output = [contract_factory, contract_factory], ["HEADER", "CONTRACT", "CONTRACT", "TRAIL"],
    assert (list(exporter.export(header_factory, trail_factory, contracts)) == expected_output)


def test_export_error_cases_one_contract(
    exporter,
    header_factory,
    trail_factory,
    contract_factory,
):
    contracts, expected_output = [contract_factory], ["HEADER", "CONTRACT", "TRAIL"]
    assert (list(exporter.export(header_factory, trail_factory, contracts)) == expected_output)


def test_export_error_cases_no_contracts(
    exporter,
    header_factory,
    trail_factory,
):
    contracts, expected_output = [], ["HEADER", "TRAIL"]
    assert (list(exporter.export(header_factory, trail_factory, contracts)) == expected_output)
