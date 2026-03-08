"""
Day 05 - Session: Cart Page Object
====================================
Page object for the shopping cart page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page object for the cart page."""

    # ── Locators ────────────────────────────────────────────────────────────
    TITLE = (By.ID, "cart-title")
    CART_TABLE = (By.ID, "cart-table")
    CART_ROWS = (By.CLASS_NAME, "cart-row")
    PRODUCT_NAMES = (By.CLASS_NAME, "cart-product-name")
    GRAND_TOTAL = (By.ID, "grand-total")
    CHECKOUT_BUTTON = (By.ID, "checkout-btn")
    EMPTY_CART = (By.ID, "empty-cart")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    # ── Actions ─────────────────────────────────────────────────────────────
    def open(self):
        return super().open("/cart")

    def get_cart_items(self):
        try:
            rows = self.find_all(self.CART_ROWS)
            items = []
            for row in rows:
                items.append({
                    "name": row.find_element(*self.PRODUCT_NAMES.__class__(By.CLASS_NAME, "cart-product-name")).text
                    if False else row.find_element(By.CLASS_NAME, "cart-product-name").text,
                    "quantity": row.find_element(By.CLASS_NAME, "quantity-value").text,
                })
            return items
        except Exception:
            return []

    def get_item_names(self):
        try:
            return [el.text for el in self.find_all(self.PRODUCT_NAMES)]
        except Exception:
            return []

    def get_grand_total(self):
        return self.get_text(self.GRAND_TOTAL)

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        return self

    def is_empty(self):
        try:
            return self.find_visible(self.EMPTY_CART).is_displayed()
        except Exception:
            return False

    def get_item_count(self):
        try:
            return len(self.find_all(self.CART_ROWS))
        except Exception:
            return 0
