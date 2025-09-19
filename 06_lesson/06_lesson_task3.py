from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 25)
waiter.until(lambda d: len(d.find_elements(
    By.CSS_SELECTOR, "#image-container img")) == 4)
images = driver.find_elements(
    By.CSS_SELECTOR, "#image-container img")
print(len(images))
src_txt = images[2].get_attribute("src")
print(src_txt)
driver.quit()
