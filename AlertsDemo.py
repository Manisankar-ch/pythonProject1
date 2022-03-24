import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert



driver = webdriver.Chrome(r"E:\browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_id("alertbtn").click()
time.sleep(5)
aler=Alert(driver.switch_to_alert())
aler.accept()
driver.close()