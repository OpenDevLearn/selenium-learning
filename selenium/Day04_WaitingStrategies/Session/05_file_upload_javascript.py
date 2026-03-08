"""
Day 04 - Session Program 5: File Upload & JavaScript Execution
================================================================
Upload files and run JavaScript commands.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import tempfile
import time

driver = webdriver.Chrome()
driver.maximize_window()

# ═══════════════════════════════════════════════════════════════════════════
# Part 1: FILE UPLOAD
# ═══════════════════════════════════════════════════════════════════════════
print("=== FILE UPLOAD ===\n")

# Create a temporary test file to upload
test_file = os.path.join(tempfile.gettempdir(), "test_upload.txt")
with open(test_file, "w") as f:
    f.write("This is a test file for Selenium upload practice.\n")
print(f"Created test file: {test_file}")

driver.get("http://localhost:5000/file-upload")
time.sleep(1)

# File upload is done by sending the file path to the <input type="file">
file_input = driver.find_element(By.ID, "file")
file_input.send_keys(test_file)

# Submit the form
driver.find_element(By.ID, "upload-btn").click()
time.sleep(1)

# Check for success message
message = driver.find_element(By.ID, "upload-message").text
print(f"Upload result: {message}")


# ═══════════════════════════════════════════════════════════════════════════
# Part 2: JAVASCRIPT EXECUTION
# ═══════════════════════════════════════════════════════════════════════════
print("\n\n=== JAVASCRIPT EXECUTION ===\n")

driver.get("http://localhost:5000/products")
time.sleep(1)

# ── Scroll to bottom of page ────────────────────────────────────────────────
print("1. Scrolling to bottom...")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(0.5)
print("   Scrolled!")

# ── Scroll to top ───────────────────────────────────────────────────────────
print("2. Scrolling to top...")
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(0.5)

# ── Scroll to specific element ──────────────────────────────────────────────
print("3. Scrolling to specific element...")
element = driver.find_element(By.ID, "product-count")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(0.5)
print(f"   Scrolled to: {element.text}")

# ── Get element properties via JS ────────────────────────────────────────────
print("\n4. Getting properties via JS...")
title = driver.execute_script("return document.title;")
print(f"   Document title: {title}")

inner_text = driver.execute_script(
    "return document.getElementById('products-title').innerText;"
)
print(f"   Element text: {inner_text}")

# ── Get computed styles ──────────────────────────────────────────────────────
print("\n5. Computed styles...")
bg_color = driver.execute_script(
    "return window.getComputedStyle(document.querySelector('.navbar')).backgroundColor;"
)
print(f"   Navbar background: {bg_color}")

# ── Modify DOM (for testing purposes) ────────────────────────────────────────
print("\n6. Modifying DOM...")
driver.execute_script(
    "document.getElementById('products-title').innerText = 'Modified by JS!';"
)
modified = driver.find_element(By.ID, "products-title").text
print(f"   Modified title: {modified}")

# ── Return values from JavaScript ────────────────────────────────────────────
print("\n7. Returning values...")
product_count = driver.execute_script(
    "return document.querySelectorAll('.product-card').length;"
)
print(f"   Product cards: {product_count}")

viewport = driver.execute_script(
    "return { width: window.innerWidth, height: window.innerHeight };"
)
print(f"   Viewport: {viewport['width']}x{viewport['height']}")

# Clean up
os.remove(test_file)
driver.quit()
print("\nFile upload & JS execution examples done!")
