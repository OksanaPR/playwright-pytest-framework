from playwright.sync_api import Page


class LoginPage:

    URL = "https://www.saucedemo.com/"
    ERROR_MESSAGE = '[data-test="error"]'
    ERROR_MESSAGE_TEXT = "Epic sadface: Username and password do not match any user in this service"
    LOCKED_USER_ERROR = "Epic sadface: Sorry, this user has been locked out."
    PRODUCTS_URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def get_error_message(self):
        return self.page.locator(self.ERROR_MESSAGE)