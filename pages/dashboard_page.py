class DashboardPage:
    def __init__(self, page):
        self.page = page

    def list_projects(self):
        return self.page.locator(".project-card").all()
