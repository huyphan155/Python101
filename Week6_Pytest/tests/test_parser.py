import pytest

from apps.parser import parse_log
from apps.models import ErrorLog

@pytest.fixture
def sample_error_log():
    return "ERROR: UART timeout"

@pytest.fixture
def sample_error_object():
    return ErrorLog(
        level="ERROR",
        message="UART timeout",
        error_code=1001
    )

def test_parse_log_ok(sample_error_log):
    log = parse_log(sample_error_log)

    assert log.level == "ERROR"
    assert log.message == "UART timeout"

def test_parse_log_invalid():
    with pytest.raises(ValueError):
        parse_log("UART timeout")

def test_error_log_code(sample_error_object):
    assert sample_error_object.level == "ERROR"
    assert sample_error_object.message == "UART timeout"
    assert sample_error_object.error_code == 1001