import pytest


@pytest.fixture(autouse=True)
def run_around_tests():
    print("\n--- Test start ---")
    yield
    print("\n--- Finish test ---")
