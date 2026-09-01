import pytest

from api.products_client import ProductsClient
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.fixture()
def default_price():
    return 100

@pytest.fixture
def standard_discount():
    return 10

@pytest.fixture
def expensive_price():
    return 500

@pytest.fixture
def vip_discount():
    return 25

@pytest.fixture
def sample_list():
    print("Creating list")
    data = []

    yield data
    print("Destroying list")

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def products_page(page):
    return ProductsPage(page)

@pytest.fixture
def products_client():
    return ProductsClient()

@pytest.fixture
def product_service(products_client):
    return ProductService(products_client)