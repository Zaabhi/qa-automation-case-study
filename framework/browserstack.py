from playwright.sync_api import sync_playwright

class BrowserStackSession:
    def __init__(self, username, access_key, os="osx", os_version="catalina", browser="chrome"):
        self.username = username
        self.access_key = access_key
        self.capabilities = {
            "browser": browser,
            "os": os,
            "os_version": os_version,
            "name": "WorkflowPro Test",
            "build": "Playwright-BrowserStack"
        }

    def create_session(self):
        playwright = sync_playwright().start()
        browser = playwright.chromium.connect_over_cdp(
            f"wss://{self.username}:{self.access_key}@cdp.browserstack.com/playwright"
        )
        return browser.new_page()
