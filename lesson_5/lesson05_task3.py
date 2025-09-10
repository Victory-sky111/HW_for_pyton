from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("http://the-internet.herokuapp.com/inputs")
search_input = driver.find_element(By.CSS_SELECTOR, "input")
search_input.send_keys("Sky")
sleep(4)
search_input.clear()
search_input.send_keys("Pro")
sleep(4)
search_input.clear()
sleep(2)
driver.quit()
