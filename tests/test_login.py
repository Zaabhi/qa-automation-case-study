import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_login_valid(driver, config, test_data):
    lp = LoginPage(driver)
    lp.load(config['base_url'])
    creds = test_data['valid_user']
    lp.login(creds['username'], creds['password'])
    assert lp.is_logged_in(), "Expected to be logged in with valid credentials"

def test_login_invalid(driver, config, test_data):
    lp = LoginPage(driver)
    lp.load(config['base_url'])
    creds = test_data['invalid_user']
    lp.login(creds['username'], creds['password'])
    # For OrangeHRM demo, invalid attempt keeps you on login page and shows errors; simple assert:
    assert not lp.is_logged_in(), "Expected login to fail with invalid credentials"
