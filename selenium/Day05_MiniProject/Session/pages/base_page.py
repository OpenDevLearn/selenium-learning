"""
Day 05 - Session: Base Page Object
====================================
The foundation class for all page objects.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

BASE_URL = "http://localhost:5000"


class BasePage:
    """Base class that all page objects inherit from."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, path=""):
        self.driver.get(f"{BASE_URL}{path}")
        return self

    def find(self, locator):
        """Find element with explicit wait for presence."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        """Find element with explicit wait for visibility."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        """Find element with explicit wait for clickability."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator):
        """Find all elements matching the locator."""
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator):
        element = self.find_clickable(locator)
        try:
            element.click()
        except Exception:
            # Dismiss any overlays and retry with scroll + JS click
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            import time
            time.sleep(0.3)
            try:
                element.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", element)
        return self

    def type_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        return self

    def get_text(self, locator):
        return self.find_visible(locator).text

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def wait_for_url(self, text):
        self.wait.until(EC.url_contains(text))
        return self

    def take_screenshot(self, name):
        filepath = os.path.join(SCREENSHOT_DIR, f"{name}.png")
        self.driver.save_screenshot(filepath)
        return filepath
