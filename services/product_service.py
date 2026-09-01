from api.products_client import ProductsClient
from models.product_response import ProductResponse


class ProductService:
    def __init__(self, products_client: ProductsClient):
        self.products_client = products_client

    def get_product(self, product_id: int) -> ProductResponse:
        response = self.products_client.get_product(product_id)

        response.raise_for_status()

        return ProductResponse.model_validate(
            response.json()
        )