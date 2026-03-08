"""
Day 03 - Session Program 3: JavaScript Alerts, Confirms & Prompts
===================================================================
Handle browser dialogs using driver.switch_to.alert.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:5000/interactions")
time.sleep(1)

# ── 1. Simple Alert ─────────────────────────────────────────────────────────
print("=== 1. Simple Alert ===")
driver.find_element(By.ID, "alert-btn").click()
time.sleep(0.5)

alert = driver.switch_to.alert
print(f"Alert text: '{alert.text}'")
alert.accept()  # Click OK
print("Alert accepted (OK clicked)")

# ── 2. Confirm Dialog ───────────────────────────────────────────────────────
print("\n=== 2. Confirm Dialog ===")

# Accept the confirm
driver.find_element(By.ID, "confirm-btn").click()
time.sleep(0.5)
confirm = driver.switch_to.alert
print(f"Confirm text: '{confirm.text}'")
confirm.accept()  # Click OK
time.sleep(0.5)
result = driver.find_element(By.ID, "alert-result").text
print(f"Result after accept: '{result}'")

# Dismiss the confirm
driver.find_element(By.ID, "confirm-btn").click()
time.sleep(0.5)
confirm = driver.switch_to.alert
confirm.dismiss()  # Click Cancel
time.sleep(0.5)
result = driver.find_element(By.ID, "alert-result").text
print(f"Result after dismiss: '{result}'")

# ── 3. Prompt Dialog ────────────────────────────────────────────────────────
print("\n=== 3. Prompt Dialog ===")
driver.find_element(By.ID, "prompt-btn").click()
time.sleep(0.5)

prompt = driver.switch_to.alert
print(f"Prompt text: '{prompt.text}'")
prompt.send_keys("Selenium Student")  # Type into the prompt
prompt.accept()
time.sleep(0.5)
result = driver.find_element(By.ID, "alert-result").text
print(f"Result after prompt: '{result}'")

# Cancel a prompt
driver.find_element(By.ID, "prompt-btn").click()
time.sleep(0.5)
prompt = driver.switch_to.alert
prompt.dismiss()
time.sleep(0.5)
result = driver.find_element(By.ID, "alert-result").text
print(f"Result after cancel: '{result}'")

driver.quit()
print("\nAlert handling done!")
