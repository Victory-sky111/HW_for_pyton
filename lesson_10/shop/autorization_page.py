import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutorizationPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://www.saucedemo.com/"

        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открыт сайт интерент магазина")
    def open(self) -> None:
        self.driver.get(self.url)

    @allure.step("Вводим логин {user} и пароль {password} для авторизации")
    # @allure.step("Нажимаем кнопку Login для входа в аккаунт")
    def login(self, user, password) -> None:
        self.wait.until(EC.visibility_of_element_located(
            self.username)).send_keys(user)
        self.driver.find_element(*self.password).send_keys(password)
    # @allure.step("Нажимаем кнопку Login для входа в аккаунт")
        self.driver.find_element(*self.login_button).click()
