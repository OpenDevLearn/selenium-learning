"""
Day 01 - Session Program 4: Page Properties
=============================================
Learn how to extract page properties: title, URL, page source, window handles.
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://localhost:5000")

# ── Page Properties ─────────────────────────────────────────────────────────
print("=== Page Properties ===")
print(f"Title       : {driver.title}")
print(f"Current URL : {driver.current_url}")
print(f"Page source : {len(driver.page_source)} characters")

# ── Window Information ──────────────────────────────────────────────────────
print("\n=== Window Info ===")
size = driver.get_window_size()
print(f"Window size     : {size['width']}x{size['height']}")

position = driver.get_window_position()
print(f"Window position : x={position['x']}, y={position['y']}")

# ── Resize and reposition ──────────────────────────────────────────────────
driver.set_window_size(800, 600)
print(f"\nAfter resize    : {driver.get_window_size()}")

driver.set_window_position(100, 100)
print(f"After reposition: {driver.get_window_position()}")

# Maximize again
driver.maximize_window()
print(f"After maximize  : {driver.get_window_size()}")

# ── Window Handle ───────────────────────────────────────────────────────────
print(f"\nWindow handle: {driver.current_window_handle}")

driver.quit()
print("\nDone!")
