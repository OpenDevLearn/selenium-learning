"""
Day 05 - Session: Register Page Object
========================================
Page object for the registration page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):
    """Page object for the registration page."""

    # ── Locators ────────────────────────────────────────────────────────────
    FULL_NAME = (By.ID, "full_name")
    USERNAME = (By.ID, "username")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "confirm_password")
    REGISTER_BUTTON = (By.ID, "register-btn")
    ERROR_MESSAGE = (By.ID, "register-error")
    SUCCESS_MESSAGE = (By.ID, "register-success")
    LOGIN_LINK = (By.ID, "login-link")

    # ── Actions ─────────────────────────────────────────────────────────────
    def open(self):
        return super().open("/register")

    def register(self, full_name, username, email, password, confirm_password=None):
        self.type_text(self.FULL_NAME, full_name)
        self.type_text(self.USERNAME, username)
        self.type_text(self.EMAIL, email)
        self.type_text(self.PASSWORD, password)
        self.type_text(self.CONFIRM_PASSWORD, confirm_password or password)
        self.click(self.REGISTER_BUTTON)
        return self

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def is_success_displayed(self):
        try:
            return self.find_visible(self.SUCCESS_MESSAGE).is_displayed()
        except Exception:
            return False
