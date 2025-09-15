```markdown
# Test Plan

## Objective

Validate core functionality of the sample web application (login, checkout flow) via automation.

## Scope

- Login: valid & invalid credentials
- Checkout: basic flow (search, add to cart, proceed to checkout) — demo stub included

## Out of scope

- Performance/load testing
- Security testing
- Accessibility testing

## Test Strategy

- Automation for smoke & regression tests
- Manual exploratory testing for UI/UX issues

## Test Environment

- Browser: Chrome (local)
- OS: Developer machine / CI runner

## Tools

- Selenium (Python)
- PyTest
- webdriver-manager
- pytest-html

## Entry Criteria

- Application URL is reachable
- Test environment ready, dependencies installed

## Exit Criteria

- All critical tests pass
- No blocking defects in tested flows

## Deliverables

- Test cases (in repo)
- Automated scripts
- Reports (HTML)
```
