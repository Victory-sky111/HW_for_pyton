import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from buy_page import BuyPage


class CartPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.checkout_button = (By.ID, "checkout")

    @allure.step("Ждем активацию кнопки Chekout и нажимаем её")
    def to_checkout(self) -> BuyPage:
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)).click()
        return BuyPage(self.driver)
