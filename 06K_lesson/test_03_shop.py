from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    wait = WebDriverWait(driver, 20)

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack")))
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-onesie")))
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "shopping_cart_link"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.ID, "checkout"))).click()

    driver.find_element(By.ID, "first-name").send_keys("Victory")
    driver.find_element(By.ID, "last-name").send_keys("Sh")
    driver.find_element(By.ID, "postal-code").send_keys("143900")
    wait.until(EC.element_to_be_clickable(
        (By.ID, "continue"))).click()

    total = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "summary_total_label")))
    s = total.text
    assert s == "Total: $58.29", f"{s} Итоговая сумма посчитана неверно"
    print(f"Итоговая сумма {s}")

    driver.quit()
