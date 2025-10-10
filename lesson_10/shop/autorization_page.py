import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutorizationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://www.saucedemo.com/"

        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.title("Открытие браузера")
    @allure.story("Открываем браузер с необходимым сайтом")
    def open(self):
        self.driver.get(self.url)

    @allure.title("Авторизация")
    @allure.story("Вводим логин и пароль для авторизации")
    def login(self, user, password):
        self.wait.until(EC.visibility_of_element_located(
            self.username)).send_keys(user)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()