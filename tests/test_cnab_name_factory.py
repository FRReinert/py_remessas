import pytest
from datetime import datetime
from cnab.cnab import CnabName

CURRENT_DATE = datetime.now()
CURRENT_DAY = str(CURRENT_DATE.day).zfill(2)
CURRENT_MONTH = str(CURRENT_DATE.month).zfill(2)
SHUFFLE_DAY = str(int(CURRENT_DAY) + 1 if int(CURRENT_DAY) < 28 else int(CURRENT_DAY) - 1).zfill(2)


@pytest.fixture
def cnab_name():
    return CnabName(
        last_used_filename="21010101.abc", service_prefix="AB", extension="XYZ"
    )


# Happy path tests
@pytest.mark.parametrize(
    "last_used_filename, service_prefix, extension, first_file, expected",
    [
        (f"CB{CURRENT_DAY}{CURRENT_MONTH}EF.abc", "AB", "XYZ", False, f"AB{CURRENT_DAY}{CURRENT_MONTH}F0.XYZ"),
        (f"CB{SHUFFLE_DAY}{CURRENT_MONTH}FF.abc", "AB", "XYZ", True, f"AB{CURRENT_DAY}{CURRENT_MONTH}00.XYZ"),
    ],
    ids=["test not the first file of the day", "test first file of the day"],
)
def test_make_name_happy_path(
    cnab_name, last_used_filename, service_prefix, extension, first_file, expected
):
    cnab_name.last_used_filename = last_used_filename
    cnab_name.service_prefix = service_prefix
    cnab_name.extension = extension
    cnab_name.first_file = first_file
    result = cnab_name.make_name()
    assert result == expected


@pytest.mark.parametrize(
    "last_used_filename, service_prefix, extension, first_file",
    [
        ("21010101.abc", "A", "XYZ", False),
        ("21010101.abc", "0", "XYZ", False),
        ("21010101.abc", "A0", "XYZ", False),
        ("21010101.abc", "$$", "XYZ", False),
        ("21010101.abc", "AB", "XY", False),
        ("21010101ZZZ.abc", "AB", "XYZ", False),
    ],
    ids=[
        "test invalid service prefix with one letter",
        "test invalid service prefix with one number",
        "test invalid service prefix with only numbers",
        "test invalid service prefix with special chars",
        "test invalid extension",
        "test invalid file length"
    ]
)
def test_make_name_error_cases(
    cnab_name, last_used_filename, service_prefix, extension, first_file
):
    cnab_name.last_used_filename = last_used_filename
    cnab_name.service_prefix = service_prefix
    cnab_name.extension = extension
    cnab_name.first_file = first_file

    with pytest.raises(ValueError):
        cnab_name.make_name()
