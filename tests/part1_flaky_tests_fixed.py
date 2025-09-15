import pytest
from playwright.sync_api import sync_playwright, expect

def test_user_login_fixed():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://app.workflowpro.com/login", wait_until="domcontentloaded")
        page.fill("#email", "admin@company1.com")
        page.fill("#password", "password123")
        page.click("#login-btn")

        expect(page).to_have_url("**/dashboard", timeout=10000)
        expect(page.locator(".welcome-message")).to_be_visible(timeout=10000)

        browser.close()

def test_multi_tenant_access_fixed():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://app.workflowpro.com/login", wait_until="domcontentloaded")
        page.fill("#email", "user@company2.com")
        page.fill("#password", "password123")
        page.click("#login-btn")

        page.wait_for_selector(".project-card", timeout=15000)
        projects = page.locator(".project-card").all()

        assert all("Company2" in project.text_content() for project in projects)

        browser.close()
