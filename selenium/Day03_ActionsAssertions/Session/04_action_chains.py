"""
Day 03 - Session Program 4: ActionChains — Hover, Double Click, Right Click
==============================================================================
Advanced user interactions using ActionChains.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:5000/interactions")
time.sleep(1)

actions = ActionChains(driver)

# ── 1. Hover (move_to_element) ──────────────────────────────────────────────
print("=== 1. Hover Action ===")
hover_card = driver.find_element(By.ID, "hover-card-1")
actions.move_to_element(hover_card).perform()
time.sleep(1)

# After hover, hidden content should appear
hidden_text = hover_card.find_element(By.CLASS_NAME, "hover-info")
print(f"Hidden element displayed after hover? {hidden_text.is_displayed()}")
print(f"Hidden text: {hidden_text.text}")

# ── 2. Double Click ─────────────────────────────────────────────────────────
print("\n=== 2. Double Click ===")
dbl_btn = driver.find_element(By.ID, "double-click-btn")
actions.double_click(dbl_btn).perform()
time.sleep(0.5)

result = driver.find_element(By.ID, "click-result").text
print(f"Result: '{result}'")

# ── 3. Right Click (Context Click) ──────────────────────────────────────────
print("\n=== 3. Right Click ===")
right_click_area = driver.find_element(By.ID, "right-click-area")
actions.context_click(right_click_area).perform()
time.sleep(0.5)

result = driver.find_element(By.ID, "click-result").text
print(f"Result: '{result}'")

# ── 4. Click and Hold + Release ──────────────────────────────────────────────
print("\n=== 4. Drag and Drop ===")
source = driver.find_element(By.ID, "drag-item-1")
target = driver.find_element(By.ID, "drag-target")

# Method 1: drag_and_drop
actions.drag_and_drop(source, target).perform()
time.sleep(0.5)

# Check if item was moved to target
target_items = target.find_elements(By.CLASS_NAME, "draggable-item")
print(f"Items in drop target: {len(target_items)}")

# ── 5. Dropdown Menu Interaction ─────────────────────────────────────────────
print("\n=== 5. Dropdown Menu ===")
dropdown_btn = driver.find_element(By.ID, "dropdown-btn")
dropdown_btn.click()
time.sleep(0.5)

items = driver.find_elements(By.CSS_SELECTOR, "#dropdown-menu .dropdown-item")
print(f"Dropdown items: {[item.text for item in items]}")

# Click an item
items[0].click()
time.sleep(0.5)

# ── 6. Keyboard Actions ─────────────────────────────────────────────────────
print("\n=== 6. Keyboard Actions ===")
from selenium.webdriver.common.keys import Keys

kb_input = driver.find_element(By.ID, "keyboard-input")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", kb_input)
time.sleep(0.3)
kb_input.click()

# Type with ActionChains
actions.send_keys_to_element(kb_input, "Hello").perform()
time.sleep(0.3)
print(f"Typed: '{kb_input.get_attribute('value')}'")

# Select all and delete
actions.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
actions.send_keys(Keys.DELETE).perform()
time.sleep(0.3)
print(f"After select-all + delete: '{kb_input.get_attribute('value')}'")

# Type new text
actions.send_keys_to_element(kb_input, "Selenium").perform()
print(f"New value: '{kb_input.get_attribute('value')}'")

driver.quit()
print("\nActionChains examples done!")
