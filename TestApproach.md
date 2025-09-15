# Test Approach

## Framework

- PyTest for test runner and assertions
- Selenium WebDriver for browser automation
- Page Object Model (POM) for maintainability

## Structure

- `pages/` contains POM classes (one class per page)
- `tests/` contains PyTest test modules
- `test-data/` holds JSON data used by tests
- `configs/` holds YAML config to control base_url and headless mode

## Reporting

- pytest-html for an HTML report
- CI will run tests and store artifacts

## Data & Locators

- Test data in JSON files
- Locators encapsulated in Page classes

## Improvements / Future Work

- Add API tests (requests or REST Assured)
- Add cross-browser matrix (BrowserStack/SauceLabs)
- Replace webdriver-manager with remote grid in CI for scalability
