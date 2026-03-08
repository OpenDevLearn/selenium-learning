"""
Day 03 - Session Program 2: Checkboxes, Radio Buttons & Complete Form
=======================================================================
Automate filling out the entire practice form.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:5000/practice-forms")
time.sleep(1)

# ── Text inputs ─────────────────────────────────────────────────────────────
driver.find_element(By.ID, "first_name").send_keys("Rahul")
driver.find_element(By.ID, "last_name").send_keys("Sharma")
driver.find_element(By.ID, "email").send_keys("rahul@example.com")

# ── Date input ──────────────────────────────────────────────────────────────
driver.find_element(By.ID, "dob").send_keys("01/15/2000")

# ── Radio buttons ───────────────────────────────────────────────────────────
male_radio = driver.find_element(By.ID, "gender-male")
print(f"Male radio selected before click? {male_radio.is_selected()}")
male_radio.click()
print(f"Male radio selected after click?  {male_radio.is_selected()}")

# ── Checkboxes ──────────────────────────────────────────────────────────────
reading_cb = driver.find_element(By.ID, "hobby-reading")
sports_cb = driver.find_element(By.ID, "hobby-sports")

reading_cb.click()
sports_cb.click()
print(f"\nReading checked? {reading_cb.is_selected()}")
print(f"Sports checked?  {sports_cb.is_selected()}")

# Toggle: click again to uncheck
sports_cb.click()
print(f"Sports after uncheck? {sports_cb.is_selected()}")
sports_cb.click()  # Re-check for submission

# ── Dropdown ────────────────────────────────────────────────────────────────
Select(driver.find_element(By.ID, "country")).select_by_visible_text("India")

# ── Range slider ────────────────────────────────────────────────────────────
slider = driver.find_element(By.ID, "experience")
# Use JavaScript to set slider value
driver.execute_script("arguments[0].value = 5; arguments[0].dispatchEvent(new Event('input'));", slider)
print(f"\nSlider value: {slider.get_attribute('value')}")

# ── Color picker ────────────────────────────────────────────────────────────
color = driver.find_element(By.ID, "color")
driver.execute_script("arguments[0].value = '#ff5733';", color)

# ── Textarea ────────────────────────────────────────────────────────────────
driver.find_element(By.ID, "message").send_keys("This is a test message.\nLine 2 of the message.")

# ── Terms checkbox ──────────────────────────────────────────────────────────
terms_cb = driver.find_element(By.ID, "agree_terms")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", terms_cb)
time.sleep(0.3)
driver.execute_script("arguments[0].click();", terms_cb)

# ── Check disabled & readonly fields ────────────────────────────────────────
disabled = driver.find_element(By.ID, "disabled-field")
readonly = driver.find_element(By.ID, "readonly-field")
print(f"\nDisabled field enabled? {disabled.is_enabled()}")
print(f"Readonly field value:   {readonly.get_attribute('value')}")

# ── Submit the form ─────────────────────────────────────────────────────────
print("\nSubmitting form...")
submit_btn = driver.find_element(By.ID, "submit-btn")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
time.sleep(0.3)
driver.execute_script("arguments[0].click();", submit_btn)
time.sleep(1)

# ── Verify the result ───────────────────────────────────────────────────────
print("\n=== Form Results ===")
print(f"First Name: {driver.find_element(By.ID, 'res-first').text}")
print(f"Last Name:  {driver.find_element(By.ID, 'res-last').text}")
print(f"Email:      {driver.find_element(By.ID, 'res-email').text}")
print(f"Gender:     {driver.find_element(By.ID, 'res-gender').text}")
print(f"Hobbies:    {driver.find_element(By.ID, 'res-hobbies').text}")
print(f"Country:    {driver.find_element(By.ID, 'res-country').text}")
print(f"Experience: {driver.find_element(By.ID, 'res-experience').text}")

driver.quit()
print("\nForm automation done!")
