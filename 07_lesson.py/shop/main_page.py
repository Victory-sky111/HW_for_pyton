from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.backpack)).click()
        self.driver.find_element(*self.tshirt).click()
        self.driver.find_element(*self.onesie).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_button).click()
        self.wait.until(EC.visibility_of_element_located(self.checkout_button))
