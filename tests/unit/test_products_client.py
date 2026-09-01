import pytest
import requests
from unittest.mock import Mock, patch

from api.products_client import ProductsClient


@pytest.mark.parametrize(
    "product_id, status_code",
    [
        (1, 200),
        (999, 404),
    ],
)
def test_get_product_calls_expected_endpoint(product_id, status_code):
    client = ProductsClient()
    mock_response = Mock()
    mock_response.status_code = status_code

    with patch("api.products_client.requests.get", return_value=mock_response) as mock_get:
        response = client.get_product(product_id)

    assert response is mock_response
    mock_get.assert_called_once_with(
        f"{ProductsClient.BASE_URL}/products/{product_id}",
        timeout=10,
    )


@pytest.mark.parametrize(
    "error",
    [
        requests.exceptions.Timeout(),
        requests.exceptions.ConnectionError(),
    ],
)
def test_get_product_propagates_requests_errors(error):
    client = ProductsClient()

    with patch("api.products_client.requests.get", side_effect=error):
        with pytest.raises(type(error)):
            client.get_product(1)

