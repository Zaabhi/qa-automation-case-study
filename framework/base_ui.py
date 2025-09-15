from playwright.sync_api import Page, expect

class BaseUI:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def goto(self, path: str):
        self.page.goto(f"{self.base_url}{path}")

    def login(self, email, password):
        self.goto("/login")
        self.page.fill("#email", email)
        self.page.fill("#password", password)
        self.page.click("#login-btn")
        expect(self.page.locator(".welcome-message")).to_be_visible()
