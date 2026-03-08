"""
Day 03 - Homework Exercise 5 (Challenge): Shopping Cart Workflow
=================================================================
TASK: Automate a complete shopping cart workflow:

  1. Login with testuser / password123
  2. Navigate to the Products page
  3. Add the first 3 products to the cart (click "Add to Cart" for each)
  4. Navigate to the Cart page
  5. Verify:
     - There are exactly 3 items in the cart
     - Each product name matches what you added
     - Print the grand total
  6. Increase the quantity of the first item by clicking "+"
  7. Remove the last item
  8. Verify the cart updated correctly (2 items, new total)
  9. Click "Checkout"
  10. Verify the success message appears
  11. Go back to Cart and verify it is empty

Print the result of each verification step.

Write your code below:
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# YOUR CODE HERE
