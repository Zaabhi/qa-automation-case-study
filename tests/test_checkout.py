import pytest
# This is a stub/demo test representing a checkout flow.
# The OrangeHRM demo does not have a shopping checkout — so this test acts as an example template.
# Replace selectors and steps for your real application.

def test_checkout_template(driver, config, test_data):
    """
    Template test: shows how you'd write a checkout end-to-end test.
    Replace with real locators and steps for your application.
    """
    base_url = config['base_url']
    driver.get(base_url)
    # Placeholder assertions to show structure
    assert "OrangeHRM" in driver.title or True
    # Example usage of test data:
    product_name = test_data['checkout']['product_name']
    assert isinstance(product_name, str)
