import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize(
    "username, password",

    [
        ("standard_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
        ("visual_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("error_user","secret_sauce")
        ]
)
def test_login_with_valid_users(login_page,username, password):
    login_page.open()
    login_page.login(username, password)
    assert login_page.page.url == login_page.PRODUCTS_URL


@pytest.mark.parametrize(
    "username, password",

    [
        ("no_existing_user", "secret_sauce"),
        ("standard_user", "no_existing_password"),
        ]
)
def test_login_with_invalid_data(login_page,username, password):
    login_page.open()
    login_page.login(username, password)
    expect (login_page.get_error_message()).to_have_text(login_page.ERROR_MESSAGE_TEXT)

def test_login_with_locked_user(login_page):
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    expect (login_page.get_error_message()).to_have_text(login_page.LOCKED_USER_ERROR)