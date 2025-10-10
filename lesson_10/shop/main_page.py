import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cart_page import CartPage


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_button = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_to_cart(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.cart_button)).click()
        return CartPage(self.driver)