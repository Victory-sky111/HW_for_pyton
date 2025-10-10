import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BuyPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_out_form(self, first, last, zip_code):
        self.wait.until(
            EC.visibility_of_element_located(
                self.first_name)).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()
        self.wait.until(EC.visibility_of_element_located(self.total_label))

    def get_total(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.total_label)).text
        return element.replace("Total: ", "").strip()