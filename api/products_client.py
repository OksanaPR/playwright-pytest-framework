import requests


class ProductsClient:
    BASE_URL = "https://dummyjson.com"

    def get_product(self, product_id: int):
        return requests.get(
            f"{self.BASE_URL}/products/{product_id}",
            timeout=10,
        )


