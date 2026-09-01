from playwright.sync_api import Page, expect


class ProductsPage:
    URL = "https://www.saucedemo.com/inventory.html"

    PRODUCTS_TITLE = '[data-test="title"]'
    SHOPPING_CART = '[data-test="shopping-cart-link"]'
    CART_BADGE = '[data-test="shopping-cart-badge"]'

    ADD_TO_CART_BACKPACK = (
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    )

    def __init__(self, page: Page):
        self.page = page

    def expect_page_opened(self):
        expect(self.page).to_have_url(self.URL)

    def get_products_title(self):
        return self.page.locator(self.PRODUCTS_TITLE)

    def add_backpack_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BACKPACK).click()

    def get_cart_badge(self):
        return self.page.locator(self.CART_BADGE)