import pytest
from cnab.interfaces import ICnabLine
from cnab.exporters import FileExporter


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
        def __init__(self, contract_id):
            self.contract_id = contract_id

        def make_line(self):
            return f"CONTRACT {self.contract_id}"

    return MockContractFactory


@pytest.fixture
def file_path(tmp_path):
    return str(tmp_path / "test_file.txt")


def test_export_with_valid_data(
    header_factory, trail_factory, contract_factory, file_path
):
    contracts = [contract_factory(1), contract_factory(2), contract_factory(3)]
    FileExporter.export(header_factory, trail_factory, contracts, file_path)

    with open(file_path, "r") as fopen:
        lines = fopen.readlines()
        assert lines[0].strip() == "HEADER"
        assert lines[1].strip() == "CONTRACT 1"
        assert lines[2].strip() == "CONTRACT 2"
        assert lines[3].strip() == "CONTRACT 3"
        assert lines[4].strip() == "TRAIL"


def test_export_with_empty_contracts(header_factory, trail_factory, file_path):
    contracts = []
    FileExporter.export(header_factory, trail_factory, contracts, file_path)

    with open(file_path, "r") as fopen:
        lines = fopen.readlines()
        assert lines[0].strip() == "HEADER"
        assert lines[1].strip() == "TRAIL"


def test_export_with_invalid_file_path(header_factory, trail_factory, contract_factory):
    contracts = [contract_factory(1), contract_factory(2)]
    file_path = "/path/to/nonexistent/file.txt"

    with pytest.raises(FileNotFoundError):
        FileExporter.export(header_factory, trail_factory, contracts, file_path)
