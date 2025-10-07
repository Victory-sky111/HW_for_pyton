from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from autorization_page import AutorizationPage
from main_page import MainPage
from cart_page import CartPage
from buy_page import BuyPage


def test_sauce_demo_checkout():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    autorization_page = AutorizationPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    buy_page = BuyPage(driver)

    autorization_page.open()
    autorization_page.login("standard_user", "secret_sauce")

    main_page.add_to_cart()
    main_page.open_cart()
    cart_page.to_checkout()
    buy_page = BuyPage(driver)
    buy_page.fill_out_form("Victory", "Sh", "143900")
    total = buy_page.get_total()
    assert total == "$58.29", f"Результат {total} неверный, верный - $58.29"

    driver.quit()
