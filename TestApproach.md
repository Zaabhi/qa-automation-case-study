# Test Approach

## Framework

- PyTest for running tests
- Playwright for web UI automation
- Requests for API validation
- BrowserStack for mobile & cross-browser testing
- Page Object Model for maintainable UI tests

## Structure

- `framework/` contains base classes (API, UI, mobile)
- `pages/` contains Page Object classes
- `tests/` contains test cases organized by functionality
- `configs/` for YAML-based environment settings
- `test-data/` JSON for user credentials & tenants

## Config Management

- Switch tenants via `X-Tenant-ID` header in API & `base_url` in config
- Different roles (Admin/Manager/User) stored in test-data

## Reporting

- pytest-html for test reports
- Artifacts uploaded in CI/CD

## Missing Questions

1. Who provides test credentials (mock vs production-like)?
2. Should test data cleanup happen automatically (delete projects after creation)?
3. Do we need parallel execution?
4. Do we need Allure/advanced reporting beyond HTML?
