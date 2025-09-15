import requests

class BaseAPI:
    def __init__(self, api_url, token, tenant_id):
        self.api_url = api_url
        self.token = token
        self.tenant_id = tenant_id

    def headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "X-Tenant-ID": self.tenant_id,
            "Content-Type": "application/json"
        }

    def post(self, endpoint, body):
        return requests.post(f"{self.api_url}{endpoint}", headers=self.headers(), json=body)

    def get(self, endpoint):
        return requests.get(f"{self.api_url}{endpoint}", headers=self.headers())
