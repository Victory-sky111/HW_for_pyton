from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("http://the-internet.herokuapp.com/login")
username_input = driver.find_element(By.CSS_SELECTOR, "#username")
username_input.send_keys("tomsmith")
sleep(3)
password_input = driver.find_element(By.CSS_SELECTOR, "#password")
password_input.send_keys("SuperSecretPassword!")
sleep(3)
button = driver.find_element(By.CSS_SELECTOR, "button.radius")
button.click()
sleep(3)
message = driver.find_element(By.CSS_SELECTOR, "#flash")
print(message.text)
driver.quit()
