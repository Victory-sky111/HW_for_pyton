import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorMainPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        self.url = "https://" \
            "bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    @allure.step("Заходим на сайт калькулятора")
    def open(self) -> None:
        self.driver.get(self.url)

    @allure.step("Вводим количество: {seconds} секунд для ожидания")
    def set_delay(self, seconds) -> None:
        field = self.wait.until(
            EC.element_to_be_clickable((By.ID, "delay")))
        field.clear()
        field.send_keys(str(seconds))

    @allure.step("Нажимаем {text} на калькуляторе")
    def click(self, text) -> None:
        btn = (By.XPATH, f"//span[text() ='{text}']")
        self.wait.until(EC.element_to_be_clickable(btn)).click()

    @allure.step("Ждем результат {expected} на дисплее калькулятора")
    def wait_for_result(self, expected) -> bool:
        return self.wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), expected))

    @allure.step("Получаем результат")
    def get_result(self) -> str:
        res = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "screen")))
        return res.text.strip()
