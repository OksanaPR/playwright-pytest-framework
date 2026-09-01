# Copilot Instructions

## Running the framework

Set up the same environment used by Jenkins:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

Run all tests with `python -m pytest`. Pytest is configured in `pyproject.toml` to discover `tests/` and always generate:

- `reports/junit.xml`
- `reports/report.html`
- `allure-results/`

Run an individual test module or test with:

```bash
python -m pytest tests/api/test_products_api.py
python -m pytest tests/api/test_products_api.py::test_get_product
python -m pytest tests/ui/test_login.py -k valid_users
```

The Jenkins pipeline provisions Python dependencies, installs Chromium, runs `pytest`, and archives the report directories.

## Architecture

This is a pytest-based test automation framework organized by test level:

- `tests/ui/` exercises Sauce Demo through synchronous Playwright page objects in `pages/`. `LoginPage` encapsulates login navigation and actions; `ProductsPage` encapsulates post-login assertions and product/cart actions. UI tests receive those page objects through fixtures rather than constructing them.
- `tests/api/` calls the DummyJSON API through `ProductsClient` in `api/`. The client owns the endpoint base URL and request timeout.
- `tests/integration/` verifies the service layer. `ProductService` wraps `ProductsClient`, raises unsuccessful HTTP responses, and converts response JSON into the Pydantic `ProductResponse` model in `models/`.
- `tests/unit/` covers pure helpers, such as `utils.math_utils.discount`, using shared value and lifecycle fixtures.

`tests/conftest.py` is the composition boundary: it creates page-object fixtures from pytest-playwright's `page` fixture and connects `ProductsClient` to `ProductService`. Keep shared fixtures there so UI, API, integration, and unit tests use the same setup semantics.

## Repository conventions

- Use synchronous Playwright APIs (`playwright.sync_api`). Page objects accept and retain a typed `Page`; tests use Playwright `expect(...)` assertions for UI state.
- Keep page selectors and test-site URLs as page-object constants. Expose page behavior through methods such as `open`, `login`, and `add_backpack_to_cart`; tests should not duplicate those selectors.
- API tests assert the raw `requests` response. Service tests consume validated `ProductResponse` instances returned by `ProductService`, rather than parsing JSON themselves.
- HTTP requests specify an explicit timeout. Service methods call `response.raise_for_status()` before model validation.
- Shared test data is supplied as pytest fixtures. Stateful fixtures use `yield` so their teardown runs after each test.
- Tests contact public external services (`saucedemo.com` and `dummyjson.com`); preserve their known test credentials, expected URLs, and response assumptions when maintaining the existing scenarios.
