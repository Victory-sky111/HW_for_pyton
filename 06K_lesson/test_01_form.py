from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options

options = Options()

dr_path = r"C:\Users\V\Downloads\edgedriver_win64 (1)\msedgedriver.exe"
service = EdgeService(dr_path)
driver = webdriver.Edge(service=service)


def test_01_form():
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    wait = WebDriverWait(driver, 20)

    zip_field = wait.until(
        EC.visibility_of_element_located((By.ID, "zip-code")))
    wait.until(lambda d: "alert-danger" in (
        zip_field.get_attribute("class") or ""))
    assert "alert-danger" in (
        zip_field.get_attribute("class") or ""), "Поле Zip-code не красное"
    print("Поле Zip-code подсвечено красным")

    for name in ["first-name", "last-name", "address", "e-mail", "phone",
                 "city", "country", "job-position", "company"]:
        field = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.alert-success")))
        wait.until(lambda d, el=field: "alert-success" in (
            el.get_attribute("class") or ""))
        assert "alert-success" in (field.get_attribute("class")
                                   or ""), f"Поле {name} не зеленого цвета"
        print(f"Поле {name} подсвечено зеленым")

    driver.quit()


test_01_form()
