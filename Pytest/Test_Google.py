from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="E:/browsers/chromedriver.exe")
    driver.maximize_window()
    print("opend browser")
    yield
    driver.close()


def test_login(test_setup):
    driver.get("https://www.google.com")
    driver.find_element(By.NAME, "q").send_keys("peace")
    driver.find_element(By.NAME, "q").send_keys(Keys.RETURN)

    driver.implicitly_wait(10)
    print(driver.title)
