import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Калькулятор")
@allure.severity("blocker")
class CalculatorMainPage:
    @allure.title("Получение списка активных организаций")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        self.url = "https://" \
            "bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    @allure.title("Открытие браузера")
    @allure.story("Открываем браузер с необходимым сайтом")
    def open(self):
        self.driver.get(self.url)

    @allure.title("Введение количества секунд для ожидания")
    @allure.story("Находим поле и вводим количество секунд для ожидания")
    def set_delay(self, seconds):
        field = self.wait.until(EC.element_to_be_clickable((By.ID, "delay")))
        field.clear()
        field.send_keys(str(seconds))

    def click(self, text):
        btn = (By.XPATH, f"//span[text() ='{text}']")
        self.wait.until(EC.element_to_be_clickable(btn)).click()

    def get_result(self):
        res = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "screen")))
        return res.text.strip()

    def wait_for_result(self, expected):
        return self.wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), expected))
