"""
Day 01 - Session Program 1: Your First Selenium Script
=======================================================
Learn how to launch a browser, navigate to a URL, and close the browser.
"""

from selenium import webdriver

# Create a Chrome browser instance
driver = webdriver.Chrome()

# Navigate to the practice application
driver.get("http://localhost:5000")

# Print basic information
print(f"Page Title: {driver.title}")
print(f"Current URL: {driver.current_url}")

# Close the browser
driver.quit()

print("Browser closed successfully!")
