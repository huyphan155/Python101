import pytest

from apps.api_client import get_post
from apps.api_client import upload_all
from unittest.mock import patch
from unittest.mock import MagicMock

def test_api_magic_mock():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": 1
    }
    result = mock_response.json()
    assert result == {"id": 1}

def test_get_post():
    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "id": 1
    }

    with patch(
        "apps.api_client.requests.get",
        return_value=fake_response
    ):

        data = get_post()

        assert data["id"] == 1


def test_upload_all():

    with patch(
        "apps.api_client.upload_log"
    ) as abc:

        upload_all(
            ["A", "B", "C"]
        )

        assert abc.call_count == 3