"""
Day 05 - Session: Dashboard Page Object
=========================================
Page object for the user dashboard.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    """Page object for the dashboard page."""

    # ── Locators ────────────────────────────────────────────────────────────
    TITLE = (By.ID, "dashboard-title")
    PROFILE_USERNAME = (By.ID, "profile-username")
    PROFILE_EMAIL = (By.ID, "profile-email")
    PROFILE_FULLNAME = (By.ID, "profile-fullname")
    LOGOUT_LINK = (By.ID, "nav-logout")

    # ── Actions ─────────────────────────────────────────────────────────────
    def open(self):
        return super().open("/dashboard")

    def get_welcome_text(self):
        return self.get_text(self.TITLE)

    def get_profile_info(self):
        return {
            "username": self.get_text(self.PROFILE_USERNAME),
            "email": self.get_text(self.PROFILE_EMAIL),
            "full_name": self.get_text(self.PROFILE_FULLNAME),
        }

    def logout(self):
        self.click(self.LOGOUT_LINK)
        return self

    def is_dashboard_loaded(self):
        try:
            return self.find_visible(self.TITLE).is_displayed()
        except Exception:
            return False
