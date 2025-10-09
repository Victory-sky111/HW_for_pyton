from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPage import CalculatorMainPage


def test_calculator():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    page = CalculatorMainPage(driver)
    page.open()
    page.set_delay(3)

    page.click("7")
    page.click("+")
    page.click("8")
    page.click("=")
    assert page.wait_for_result("15")
    actual = page.get_result()
    expect = "15"
    assert actual == expect, f"Результат {actual} неверный, "
    f"результат должен быть {expect}"
    print(f"Результат {expect} появился через 45 секунд")
    driver.quit()
