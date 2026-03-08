"""
Day 04 - Session Program 3: Fluent Wait & Custom Conditions
=============================================================
Fine-grained control over wait behavior.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:5000/dynamic")

# ── Fluent Wait: Custom polling interval + ignored exceptions ────────────────
print("=== Fluent Wait ===")

# Click to add a dynamic element
driver.find_element(By.ID, "add-element-btn").click()

wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,     # Check every 0.5 seconds (default is 0.5)
    ignored_exceptions=[
        NoSuchElementException,
        StaleElementReferenceException,
    ]
)

element = wait.until(
    EC.visibility_of_element_located((By.ID, "added-element-1"))
)
print(f"Found element: {element.text}")


# ── Custom Wait Condition ────────────────────────────────────────────────────
print("\n=== Custom Wait Condition ===")

# Custom condition: wait until there are at least N items
def at_least_n_elements(locator, n):
    """Custom expected condition: wait until at least n elements are found."""
    def condition(driver):
        elements = driver.find_elements(*locator)
        if len(elements) >= n:
            return elements
        return False
    return condition

# Add a few more elements
driver.find_element(By.ID, "add-element-btn").click()
driver.find_element(By.ID, "add-element-btn").click()

elements = WebDriverWait(driver, 10).until(
    at_least_n_elements((By.CLASS_NAME, "added-element"), 3)
)
print(f"Found {len(elements)} elements (waited for at least 3)")


# ── Custom condition with lambda ─────────────────────────────────────────────
print("\n=== Lambda Wait ===")

# Wait until page title contains "Dynamic"
WebDriverWait(driver, 10).until(
    lambda d: "Dynamic" in d.title
)
print(f"Title contains 'Dynamic': {driver.title}")


# ── Timeout handling ─────────────────────────────────────────────────────────
print("\n=== Timeout Handling ===")
from selenium.common.exceptions import TimeoutException

try:
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, "nonexistent-element"))
    )
except TimeoutException:
    print("TimeoutException caught: element did not appear within 3 seconds")


# ── Page Load Timeout ────────────────────────────────────────────────────────
print("\n=== Page Load Timeout ===")

driver.set_page_load_timeout(2)  # Very short timeout

try:
    driver.get("http://localhost:5000/slow-page?delay=5")
except Exception as e:
    print(f"Page load timed out: {type(e).__name__}")

# Reset to a reasonable timeout
driver.set_page_load_timeout(30)

driver.quit()
print("\nFluent wait examples done!")
