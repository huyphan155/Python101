import pytest

from apps.parser import parse_log

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