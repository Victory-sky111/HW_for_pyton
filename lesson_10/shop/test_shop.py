import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from autorization_page import AutorizationPage
from main_page import MainPage
from cart_page import CartPage
from buy_page import BuyPage

"""Эта функция заходит на сайт интернет-магазина,
складывает товары в корзину и проверяет итоговую стоимость товаров.
Результат печатается в консоль. Параметры должны быть в консоли."""


@allure.suite("Тест 2 для домашнего задания")
@allure.epic("Интернет-магазин одежды")
@allure.title("Проверка подсчета итоговой стоимости")
@allure.story("Авторизация, заполнение корзины, внесение данных покупателя")
@allure.severity("blocker")
def test_shop_checkout() -> None:
    with allure.step("Открываем браузер"):
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()

        autorization_page = AutorizationPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        buy_page = BuyPage(driver)

    with allure.step("Открываем страницу интернет-магазина"):
        autorization_page.open()
    with allure.step("Проходим авторизацию на сайте"):
        autorization_page.login("standard_user", "secret_sauce")

    with allure.step("Добавляем товары в корзину"):
        main_page.add_to_cart()
    with allure.step("Переходим в корзину"):
        cart_page = main_page.open_cart()
    with allure.step("Переходим на страницу заполнения данных покупателя"):
        cart_page.to_checkout()
        buy_page = BuyPage(driver)
    with allure.step("Заполняем данные покупателя"):
        buy_page.fill_out_form("Victory", "Sh", "143900")
    with allure.step("Фиксруем итоговую сумму"):
        total = buy_page.get_total()
        assert total == "$58.29", f"Результат {total} неверный,верный - $58.29"
        print("Итоговая сумма $58.29")
    with allure.step("Закрываем браузер"):
        driver.quit()
