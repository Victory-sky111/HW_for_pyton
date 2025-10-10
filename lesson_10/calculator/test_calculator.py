import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPage import CalculatorMainPage

"""Эта функция заходит на сайт калькулятора,
задает время ожидания результата, складывает две цифры
и ждет результат заданное количество секунд.
Результат печатается в консоль.Параметры должны быть в консоли."""


@allure.suite("Тест 2 для домашнего задания")
@allure.epic("Калькулятор")
@allure.title("Проверка сложения")
@allure.story("Проверка работы калькулятора")
@allure.severity("blocker")
def test_calculator() -> None:

    with allure.step("Открываем браузер"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()

        page = CalculatorMainPage(driver)
    with allure.step("Открываем страницу калькулятора"):
        page.open()
    with allure.step("Устанавливаем задержку на вывод результата"):
        page.set_delay(3)

    with allure.step("Вводим данные"):
        page.click("7")
        page.click("+")
        page.click("8")
        page.click("=")
    with allure.step("Проверяем результат"):
        assert page.wait_for_result("15")
        actual = page.get_result()
        expect = "15"
    with allure.step("Выводим результат проверки в консоль"):
        assert actual == expect, f"Результат {actual} неверный, "
        f"результат должен быть {expect}"
        print(f"Результат {expect} появился через 3 секунды")
    with allure.step("Закрываем браузер"):
        driver.quit()
