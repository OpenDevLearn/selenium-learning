"""
Day 05 - Session: Products Page Object
========================================
Page object for the products page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class ProductsPage(BasePage):
    """Page object for the products page."""

    # ── Locators ────────────────────────────────────────────────────────────
    TITLE = (By.ID, "products-title")
    SEARCH_INPUT = (By.ID, "search-input")
    SEARCH_BUTTON = (By.ID, "search-btn")
    CATEGORY_FILTER = (By.ID, "category-filter")
    PRODUCT_COUNT = (By.ID, "product-count")
    PRODUCT_CARDS = (By.CLASS_NAME, "product-card")
    PRODUCT_NAMES = (By.CLASS_NAME, "product-name")
    PRODUCT_PRICES = (By.CLASS_NAME, "product-price")
    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, "add-to-cart-btn")

    # ── Actions ─────────────────────────────────────────────────────────────
    def open(self):
        return super().open("/products")

    def search_product(self, query):
        self.type_text(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)
        return self

    def filter_by_category(self, category):
        dropdown = Select(self.find(self.CATEGORY_FILTER))
        dropdown.select_by_visible_text(category)
        return self

    def get_product_count_text(self):
        return self.get_text(self.PRODUCT_COUNT)

    def get_product_names(self):
        return [el.text for el in self.find_all(self.PRODUCT_NAMES)]

    def get_product_prices(self):
        return [el.text for el in self.find_all(self.PRODUCT_PRICES)]

    def add_product_to_cart(self, index=0):
        buttons = self.find_all(self.ADD_TO_CART_BUTTONS)
        if index < len(buttons):
            buttons[index].click()
        return self

    def get_total_products(self):
        return len(self.find_all(self.PRODUCT_CARDS))
