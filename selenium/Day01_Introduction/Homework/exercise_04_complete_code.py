"""
Day 01 - Homework Exercise 4: Complete the Code
=================================================
TASK: The code below is incomplete. Fill in the blanks (marked with _____)
      to make it work correctly.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
options = _____()                              # 1. Create an Options object
options.add_argument("--window-size=1024,768")

# Create a browser instance with options
driver = webdriver._____(options=options)       # 2. Create Chrome driver

# Navigate to the practice app
driver._____(_____)                             # 3. Navigate to http://localhost:5000

# Print the title
print(f"Title: {driver._____}")                # 4. Get the page title

# Navigate to the products page
driver.get("http://localhost:5000/products")

# Get window size
size = driver._____()                          # 5. Get the window size
print(f"Window: {size['width']}x{size['height']}")

# Go back to the home page
driver._____()                                 # 6. Go back to previous page

# Print where we are now
print(f"URL after back: {driver._____}")       # 7. Get current URL

# Clean up
driver._____()                                 # 8. Quit the browser (not just close)
print("Done!")
