import pytest
from apps.models import ErrorLog


@pytest.fixture(autouse=True)
def run_around_tests():
    print("\n--- Test start ---")
    yield
    print("\n--- Finish test ---")

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