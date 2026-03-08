"""
Day 01 - Session Program 3: Browser Options
=============================================
Learn how to configure browser options: headless mode, window size, etc.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ── Example 1: Headless Mode ───────────────────────────────────────────────
print("=== Headless Mode ===")
options = Options()
options.add_argument("--headless=new")          # Run without opening a visible browser
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.get("http://localhost:5000")
print(f"Title (headless): {driver.title}")
print(f"Page source length: {len(driver.page_source)} characters")
driver.quit()


# ── Example 2: Custom Window Size ──────────────────────────────────────────
print("\n=== Custom Window Size ===")
options2 = Options()
options2.add_argument("--window-size=1920,1080")

driver2 = webdriver.Chrome(options=options2)
driver2.get("http://localhost:5000")
size = driver2.get_window_size()
print(f"Window size: {size['width']}x{size['height']}")
driver2.quit()


# ── Example 3: Disable Notifications ───────────────────────────────────────
print("\n=== Disable Notifications ===")
options3 = Options()
options3.add_argument("--disable-notifications")
options3.add_experimental_option("excludeSwitches", ["enable-logging"])

driver3 = webdriver.Chrome(options=options3)
driver3.get("http://localhost:5000")
print(f"Title: {driver3.title}")
driver3.quit()

print("\nAll examples completed!")
