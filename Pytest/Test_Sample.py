import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.service import Service
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(service=Service(executable_path="E:/browsers/chromedriver.exe"))

    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("Test completed")

def test_login(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element(By.ID,"txtUsername").send_keys("Admin")
    time.sleep(3)
    driver.find_element(By.ID,"txtPassword").send_keys("admin123")
    time.sleep(3)
    driver.find_element(By.ID,"btnLogin").click()
    time.sleep(3)
    print(driver.title)
    driver.implicitly_wait(10)
