"""
Day 03 - Session Program 6: Windows, Tabs & iFrames
=====================================================
Switching between windows/tabs and working with iframes.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# ═══════════════════════════════════════════════════════════════════════════
# Part 1: MULTIPLE WINDOWS / TABS
# ═══════════════════════════════════════════════════════════════════════════
print("=== WINDOWS & TABS ===\n")

driver.get("http://localhost:5000/interactions")
time.sleep(1)

# Remember the main window handle
main_window = driver.current_window_handle
print(f"Main window handle: {main_window}")
print(f"Total windows: {len(driver.window_handles)}")

# Open new tab via link
new_tab_link = driver.find_element(By.ID, "new-tab-link")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", new_tab_link)
time.sleep(0.3)
driver.execute_script("arguments[0].click();", new_tab_link)
time.sleep(1)

print(f"\nAfter opening new tab:")
print(f"Total windows: {len(driver.window_handles)}")

# Switch to the new window/tab
for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        break

print(f"New window title: {driver.title}")
print(f"New window URL:   {driver.current_url}")

# Read content from new window
text = driver.find_element(By.ID, "new-window-text").text
print(f"Content: {text}")

# Close new tab and switch back
driver.close()
driver.switch_to.window(main_window)
print(f"\nBack to main window: {driver.title}")
print(f"Total windows: {len(driver.window_handles)}")

# ═══════════════════════════════════════════════════════════════════════════
# Part 2: iFRAMES
# ═══════════════════════════════════════════════════════════════════════════
print("\n\n=== iFRAMES ===\n")

driver.get("http://localhost:5000/frames")
time.sleep(1)

# We're on the main page — try to access frame content first (will fail)
print("Before switching to frame:")
try:
    driver.find_element(By.ID, "frame-title")
    print("  Found element (unexpected!)")
except Exception:
    print("  Cannot find #frame-title — element is inside an iframe!")

# ── Switch to iframe by ID ──────────────────────────────────────────────────
driver.switch_to.frame("main-frame")
print("\nAfter switching to 'main-frame':")

frame_title = driver.find_element(By.ID, "frame-title").text
print(f"  Frame title: {frame_title}")

# Interact with elements inside the frame
frame_btn = driver.find_element(By.ID, "frame-btn")
frame_btn.click()
time.sleep(0.5)
result = driver.find_element(By.ID, "frame-result").text
print(f"  Button result: {result}")

# Type into input inside frame
frame_input = driver.find_element(By.ID, "frame-input")
frame_input.send_keys("Hello from inside the frame!")
print(f"  Input value: {frame_input.get_attribute('value')}")

# ── Switch back to main page ────────────────────────────────────────────────
driver.switch_to.default_content()
print("\nBack to default content (main page)")

# ── Nested iFrames ──────────────────────────────────────────────────────────
print("\n=== Nested iFrames ===")

# Switch to outer frame first
driver.switch_to.frame("outer-frame")
outer_title = driver.find_element(By.ID, "outer-frame-title").text
print(f"Outer frame title: {outer_title}")

# Now switch to the inner frame (nested inside outer)
driver.switch_to.frame("inner-frame")
inner_title = driver.find_element(By.ID, "frame-title").text
print(f"Inner frame title: {inner_title}")

# To go back, switch to parent frame (one level up)
driver.switch_to.parent_frame()
print("Back to outer frame")
outer_text = driver.find_element(By.ID, "outer-frame-text").text
print(f"Outer frame text: {outer_text}")

# Back to main page
driver.switch_to.default_content()
print("Back to main page")

driver.quit()
print("\nWindows & Frames examples done!")
