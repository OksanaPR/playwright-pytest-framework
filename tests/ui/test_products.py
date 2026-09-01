from playwright.sync_api import expect


def test_add_to_shopping_cart(login_page, products_page):
    login_page.open()
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page.expect_page_opened()
    expect(products_page.get_products_title()).to_have_text("Products")
    products_page.add_backpack_to_cart()
    expect(products_page.get_cart_badge()).to_have_text("1")
