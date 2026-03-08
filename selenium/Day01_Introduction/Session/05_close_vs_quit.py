"""
Day 01 - Session Program 5: Close vs Quit & Multiple Tabs
===========================================================
Understand the difference between close() and quit().
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Open the home page
driver.get("http://localhost:5000")
print(f"Tab 1 - Title: {driver.title}")
print(f"Window handles: {driver.window_handles}")

# Open a new tab using JavaScript
driver.execute_script("window.open('http://localhost:5000/products', '_blank');")
time.sleep(1)

print(f"\nAfter opening new tab:")
print(f"Window handles: {driver.window_handles}")
print(f"Total tabs: {len(driver.window_handles)}")

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])
print(f"\nSwitched to Tab 2 - Title: {driver.title}")

# close() only closes the CURRENT tab/window
driver.close()
print("\nAfter close(): closed only the current tab (Tab 2)")
print(f"Remaining handles: {driver.window_handles}")

# Switch back to the first tab
driver.switch_to.window(driver.window_handles[0])
print(f"Switched back to Tab 1 - Title: {driver.title}")

# quit() closes ALL windows and ends the WebDriver session
driver.quit()
print("\nAfter quit(): all windows closed and session ended")
print("""
Summary:
  driver.close() → Closes the CURRENT window/tab only
  driver.quit()  → Closes ALL windows and ends the WebDriver session
  
Always use quit() at the end of your script to clean up properly!
""")
