from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 55)


def test_02_calc():
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay = wait.until(EC.presence_of_element_located((By.ID, "delay")))
    delay.clear()
    delay.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "screen"), "15"))
    result = driver.find_element(
        By.CLASS_NAME, "screen").text
    assert result == "15", f"Результат {result} неверный"
    print(f"Результат {result} появился через 45 секунд")

    driver.quit()


test_02_calc()
