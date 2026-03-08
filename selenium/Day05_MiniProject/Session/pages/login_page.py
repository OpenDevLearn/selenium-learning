"""
Day 05 - Session: Login Page Object
=====================================
Page object for the Login page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the login page."""

    # ── Locators ────────────────────────────────────────────────────────────
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-btn")
    ERROR_MESSAGE = (By.ID, "login-error")
    REGISTER_LINK = (By.ID, "register-link")
    REMEMBER_ME = (By.ID, "remember-me")

    # ── Actions ─────────────────────────────────────────────────────────────
    def open(self):
        return super().open("/login")

    def login(self, username, password):
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self):
        try:
            return self.find_visible(self.ERROR_MESSAGE).is_displayed()
        except Exception:
            return False

    def click_register(self):
        self.click(self.REGISTER_LINK)
        return self

    def toggle_remember_me(self):
        self.click(self.REMEMBER_ME)
        return self
