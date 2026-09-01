


def test_product_service_returns_real_product(product_service):
    product = product_service.get_product(1)

    assert product.id == 1
    assert product.title
    assert product.price > 0