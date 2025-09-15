from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self, base_url):
        self.visit(base_url)

    def login(self, username, password):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.login_button)

    def is_logged_in(self):
        try:
            self.wait_for_visible(self.dashboard_header, timeout=8)
            return True
        except:
            return False
