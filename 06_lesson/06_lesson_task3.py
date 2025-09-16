from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 25)
waiter.until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, "div#image-container.col-12.py-2 img#landscape")))
images = driver.find_elements(
    By.CSS_SELECTOR, "div#image-container.col-12.py-2 img#award")
src_txt = images.get_attribute("src")
print(src_txt)
driver.quit()
