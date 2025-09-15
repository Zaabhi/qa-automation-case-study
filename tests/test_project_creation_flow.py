import pytest
from framework.base_api import BaseAPI
from framework.base_ui import BaseUI
from framework.browserstack import BrowserStackSession

API_TOKEN = "dummy_token"   # would come from secrets manager in real pipeline

@pytest.mark.integration
def test_project_creation_flow(playwright, config={"tenant_id": "company1"}):
    # Step 1: API - Create project
    api = BaseAPI(api_url="https://api.workflowpro.com", token=API_TOKEN, tenant_id=config["tenant_id"])
    project_payload = {"name": "Test Project", "description": "Created via API", "team_members": ["admin"]}
    response = api.post("/api/v1/projects", project_payload)
    assert response.status_code == 200
    project_id = response.json()["id"]

    # Step 2: Web UI Verification
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    ui = BaseUI(page, "https://company1.workflowpro.com")
    ui.login("admin@company1.com", "password123")
    expect(page.locator(f"text={project_payload['name']}")).to_be_visible()

    # Step 3: Mobile Validation (BrowserStack stub)
    # In real pipeline, we'd connect with BrowserStack iOS/Android devices
    # Example placeholder (not runnable locally without BrowserStack creds)
    # session = BrowserStackSession(USERNAME, ACCESS_KEY).create_session()
    # session.goto("https://company1.workflowpro.com")
    # assert session.locator(f"text={project_payload['name']}").is_visible()

    # Step 4: Tenant Isolation Check
    other_tenant = BaseAPI(api_url="https://api.workflowpro.com", token=API_TOKEN, tenant_id="company2")
    resp2 = other_tenant.get(f"/api/v1/projects/{project_id}")
    assert resp2.status_code == 404, "Project should not be visible in another tenant"

    browser.close()
