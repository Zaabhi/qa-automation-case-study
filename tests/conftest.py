import pytest
import yaml
import json
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

ROOT = os.path.dirname(os.path.dirname(__file__)) if os.path.basename(os.getcwd()) != 'tests' else os.getcwd()

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "../configs/config.yaml")
    with open(config_path, 'r') as fh:
        return yaml.safe_load(fh)

def load_test_data():
    td_path = os.path.join(os.path.dirname(__file__), "../test-data/sample_test_data.json")
    with open(td_path, 'r') as fh:
        return json.load(fh)

@pytest.fixture(scope='session')
def config():
    return load_config()

@pytest.fixture(scope='session')
def test_data():
    return load_test_data()

@pytest.fixture
def driver(request, config):
    chrome_options = Options()
    if config.get('headless', False):
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(config.get('implicit_wait', 5))
    yield driver
    driver.quit()
