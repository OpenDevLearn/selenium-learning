"""
Day 02 - Homework Exercise 3: Complete the Product Scraper
===========================================================
TASK: Fill in the blanks (marked with _____) to scrape product data.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:5000/products")
time.sleep(1)

# Get all product cards
cards = driver.find_elements(_____, _____)       # 1. Find all elements with class "product-card"

print(f"Found {len(cards)} products\n")

for card in cards:
    # Extract product details FROM WITHIN each card
    name = card.find_element(_____, _____).text          # 2. Find product-name class
    price = card.find_element(_____, _____).text         # 3. Find product-price class
    category = card._____(By.CLASS_NAME, "product-category").text  # 4. Method name
    stock = card.find_element(By.CLASS_NAME, _____).text # 5. Class for stock info

    print(f"Product: {name}")
    print(f"  Price:    {price}")
    print(f"  Category: {category}")
    print(f"  Stock:    {stock}")
    print()

# Total product count
count_badge = driver.find_element(By.ID, _____)  # 6. The ID of the product count badge
print(f"Badge text: {count_badge._____}")         # 7. Property to get visible text

driver.quit()
